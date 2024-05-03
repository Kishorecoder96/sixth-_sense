import time
import cv2
import numpy as np
import tensorflow as tf

try:
    from tflite_runtime.interpreter import Interpreter,load_delegate
except:
    from tf.lite.python.interpreter import Interpreter,load_delegate

class midasDepthEstimator:
    def __init__(self,voice_assistant,pi):
        self.pi = pi
        self.voice_assistant = voice_assistant
        self.i = 0
        self.fps = 0
        #self.timeLastPrediction = time.time()
        self.frameCounter = 0

        # Initialize model
        self.initializeModel()

    def initializeModel(self):
        modelPath = 'model/midasModel/midasModel_edgetpu.tflite' 
        
        self.interpreter = Interpreter(modelPath, num_threads=1)
        self.interpreter.allocate_tensors()

        # Get model info
        self.getModelInputDetails()
        self.getModelOutputDetails()

    def estimateDepth(self, image):
        input_tensor = self.prepareInputForInference(image)

        # Perform inference on the image
        rawDisparity = self.inference(input_tensor)

        # Normalize and resize raw disparity
        processedDisparity = self.processRawDisparity(rawDisparity, image.shape)

        # Draw depth image
        colorizedDisparity = self.drawDepth(processedDisparity)

        return colorizedDisparity

    def prepareInputForInference(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.img_height, self.img_width, self.img_channels = img.shape

        
        img_input = cv2.resize(img, (self.inputWidth,self.inputHeight),interpolation = cv2.INTER_CUBIC).astype(np.float32)

       
        mean=[0.485, 0.456, 0.406]
        std=[0.229, 0.224, 0.225]
        reshape_img = img_input.reshape(1, self.inputHeight, self.inputWidth,3)
        img_input = ((img_input/ 255.0 - mean) / std).astype(np.float32)
        img_input = img_input[np.newaxis,:,:,:]        

        return img_input
    

    def inference(self, img_input):
        # Peform inference
        self.interpreter.set_tensor(self.input_details[0]['index'], img_input)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self.output_details[0]['index'])
        output = output.reshape(self.outputHeight, self.outputWidth)

        return output
    

    def processRawDisparity(self, rawDisparity, img_shape):
        # Normalize estimated depth to have values between 0 and 255
        depth_min = rawDisparity.min()
        depth_max = rawDisparity.max()
        normalizedDisparity = (255 * (rawDisparity - depth_min) / (depth_max - depth_min)).astype("uint8")

        # Resize disparity map to the sam size as the image inference
        estimatedDepth = cv2.resize(normalizedDisparity, (img_shape[1], img_shape[0]), interpolation=cv2.INTER_CUBIC)

        return estimatedDepth
    

    def drawDepth(self, processedDisparity):
        return cv2.applyColorMap(processedDisparity, cv2.COLORMAP_MAGMA)
    

    def getModelInputDetails(self):
        self.input_details = self.interpreter.get_input_details()
        input_shape = self.input_details[0]['shape']
        self.inputHeight = input_shape[1]
        self.inputWidth = input_shape[2]
        self.channels = input_shape[3]


    def getModelOutputDetails(self):
        self.output_details = self.interpreter.get_output_details()
        output_shape = self.output_details[0]['shape']
        self.outputHeight = output_shape[1]
        self.outputWidth = output_shape[2]  


    def updateFps(self):
        updateRate = 1
        self.frameCounter += 1

        # Every updateRate frames calculate the fps based on the ellapsed time
        if self.frameCounter == updateRate:
            timeNow = time.time()
            ellapsedTime = timeNow - self.timeLastPrediction

            self.fps = int(updateRate/ellapsedTime)
            self.frameCounter = 0
            self.timeLastPrediction = timeNow

    def checkDistanceThreshold(self, depth_map, image_width):
   
        depth_map_meters = depth_map / 1000.0  

        # Find the minimum depth value (closest object)
        min_depth = np.min(depth_map_meters)

        # Define threshold distance (in meters)
        threshold_distance = 2 

        if min_depth < threshold_distance:
# Find the position of the object in the image
            object_position = self.getObjectPosition(depth_map, image_width)

            # Check if the distance is very close
            if min_depth <= 1:
                self.pi.setupVibrate()
            else:
                # Trigger warning with directional information
                if len(self.warning) > 1:
                    self.warning = []
                if object_position == "left":
                    self.warning.append("left")
                    self.voice_assistant.speak("Move Right")
                else:
                    self.warning.append("right")
                    self.voice_assistant.speak("Move Left")

           

    def getObjectPosition(self, depth_map, image_width):
    # Calculate the depth map's midpoint
        depth_midpoint = depth_map.shape[1] // 2
        
        # Calculate the average depth of the left and right halves of the depth map
        left_depth_avg = np.mean(depth_map[:, :depth_midpoint])
        right_depth_avg = np.mean(depth_map[:, depth_midpoint:])

        # Determine the position of the object based on the average depths
        if left_depth_avg < right_depth_avg:
            object_position = "left"
        else:
            object_position = "right"
      
        return object_position
    

    
    def run(self, frame):
        img = np.array(frame)

        # Estimate depth
        colorDepth = self.estimateDepth(img)
        
        # Get depth map
        depth_map = self.inference(self.prepareInputForInference(img))
        
        position = self.checkDistanceThreshold(depth_map, img.shape[1])

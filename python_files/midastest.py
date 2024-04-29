import cv2
import numpy as np
from midas import midasDepthEstimator
from voice import VoiceAssistant

voice_assistant = VoiceAssistant()
# Initialize depth estimation model
depthEstimator = midasDepthEstimator(voice_assistant)

# Initialize webcam
camera = cv2.VideoCapture(0)
cv2.namedWindow("Depth Image") 	
fps = 1 
freq = cv2.getTickFrequency()

while True:
    t1 = cv2.getTickCount()
    # Read frame from the webcam
    ret, img = camera.read() 

    # Estimate depth
    colorDepth = depthEstimator.estimateDepth(img)
    
    # Get depth map
    depth_map = depthEstimator.inference(depthEstimator.prepareInputForInference(img))

    # Check distance threshold
    # depthEstimator.checkDistanceThreshold(depth_map, img.shape[1])  # Pass image width for object position calculation

    # Add the depth image over the color image:
    combinedImg = cv2.addWeighted(img, 0.7, colorDepth, 0.6, 0)

    # Join the input image, the estimated depth, and the combined image
    img_out = np.hstack((img, colorDepth, combinedImg))
    # cv2.putText(img_out, "FPS: {}".format(depthEstimator.fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(img_out, "FPS: {}".format(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 2)
    # cv2.putText(img)
    # print(fps)
    position = depthEstimator.checkDistanceThreshold(depth_map, img.shape[1])
    # if position == "left":
    #     cv2.putText(combinedImg,"WARNING!! object on right", (500, 500),cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
    # elif position == "right":
    #     cv2.putText(combinedImg,"WARNING!! object on left", (500, 500),cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
    cv2.imshow("Depth Image", colorDepth)
    t2 = cv2.getTickCount()
    time1 = (t2-t1)/freq
    fps = 1/time1
    


    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()




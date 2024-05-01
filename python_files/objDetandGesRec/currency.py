
import cv2
import numpy as np
import tensorflow as tf

class ImageClassifier:
    def __init__(self, voice_assistant,model_path = 'currency.tflite', label_path = 'currency.txt'):
        self.voice_assistant = voice_assistant
        self.currency = []
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.labels = open(label_path, 'r').read().splitlines()

    def preprocess_image(self, image):
        input_details = self.interpreter.get_input_details()
        input_shape = input_details[0]['shape']
        input_data = cv2.resize(image, (input_shape[1], input_shape[2]))
        input_data = np.expand_dims(input_data, axis=0)
        input_data = (np.float32(input_data) - 127.5) / 127.5  # Normalize input
        return input_data

    def classify_image(self, image):
        input_data = self.preprocess_image(image)
        self.interpreter.set_tensor(self.interpreter.get_input_details()[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.interpreter.get_output_details()[0]['index'])
        return output_data

    def predict(self, image):
        results = self.classify_image(image)
        predicted_class = np.argmax(results)
        confidence_score = results[0][predicted_class]
        # cv2.putText(image, f'Label: {self.labels[predicted_class]}, Confidence: {confidence_score}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # cv2.imshow('Frame', image)
        if len(self.currency )  > 1:
                self.currency = []
        if (self.labels[predicted_class] == "10")and("10" not in self.currency)  :
            self.currency.append("10")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] + "rupees note")
            
        elif (self.labels[predicted_class] == "20")and("20" not in self.currency)  :
            self.currency.append("20")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] + "rupees note")

        elif (self.labels[predicted_class] == "50")and("50" not in self.currency)  :
            self.currency.append("50")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] +"rupees note")
        
        elif (self.labels[predicted_class] == "100")and("100" not in self.currency)  :
            self.currency.append("100")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] +"rupees note")

        elif (self.labels[predicted_class] == "200")and("200" not in self.currency)  :
            self.currency.append("200")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] + "rupees note")

        elif (self.labels[predicted_class] == "500")and("500" not in self.currency)  :
            self.currency.append("500")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] + "rupees note")

        elif (self.labels[predicted_class] == "2000")and("2000" not in self.currency)  :
            self.currency.append("2000")
            
            self.voice_assistant.speak("You're holding a " + self.labels[predicted_class] + "rupees note")
    

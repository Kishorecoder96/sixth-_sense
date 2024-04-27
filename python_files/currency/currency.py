import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps


class CurrencyDetection:
    def __init__(self,voice_assistant,model_path = 'model/model.savedmodel', labels_path='model/labels.txt'):
        self.voice_assistant = voice_assistant
        self.model = tf.saved_model.load(model_path)
        self.class_names = [name.split()[1] for name in open(labels_path, "r").readlines()]

    def detect_currency(self, img_path):
       
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open(img_path).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        data[0] = normalized_image_array

        infer = self.model.signatures['serving_default']

        prediction = infer(tf.constant(data))['sequential_3']
        index = np.argmax(prediction)
        
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]
       
        if confidence_score > 0.999:
            self.voice_assistant.speak(f"Your holding a {class_name} rupees")
            
        else:
            self.voice_assistant.speak("Sorry the image is not clear")

# currency_detector = CurrencyDetection()
# currency_detector.detect_currency("/Users/danny/Downloads/testmain100/IMG_1862.jpg")      
        






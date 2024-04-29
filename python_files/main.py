import time
import spacy
import cv2
import numpy as np
import threading
from server import FirebaseManager
from ocr import OCR
from piApi import piAPI
from capture import WebcamCapture
from voice import VoiceAssistant
from midas import midasDepthEstimator
from notification import NotificationSender
from stepBystep import NavigateUser
from dateandtime import DateAndTime
from currency.currency import CurrencyDetection
from gemini import GeminiVisionProAssistant,GeminiProAssistant


json_file = "message/secret.json"
nlp = spacy.load('en_core_web_sm')

voice_assistant = VoiceAssistant()
voice_assistant.start()
dba = FirebaseManager(voice_assistant)
pi = piAPI(dba,voice_assistant)
navigate = NavigateUser(voice_assistant)
webcam = WebcamCapture(voice_assistant)
datetime = DateAndTime(voice_assistant)
currency_detector = CurrencyDetection(voice_assistant)
gemini_pro_assistant = GeminiProAssistant(voice_assistant)
gemini_vision_pro_assistant = GeminiVisionProAssistant(voice_assistant)
ocr = OCR(voice_assistant)
notification = NotificationSender(voice_assistant)
depthEstimator = midasDepthEstimator(voice_assistant)

def process1():

    voice_assistant.speak("Listening")
    WAKE = "hello"
    
    while True:
        voice_input = voice_assistant.get_audio()
        print(voice_input)

        if voice_input == WAKE:
            voice_assistant.speak("Sixth Sense listening")

            while True:
                time.sleep(1)
                voice_input = voice_assistant.get_audio()
                print(voice_input)
                doc = nlp(voice_input)

                if 'photo' in [token.lemma_ for token in doc]:
                    webcam = WebcamCapture(voice_assistant)
                    image_path = webcam.capture_photo()
                    voice_assistant.speak("What would you like to do")
                    question = voice_assistant.get_audio()
                    doc = nlp(question)

                    if 'text' in [token.lemma_ for token in doc]:
                        ocr.extract_text_from_image(image_path)

                    else:
                        gemini_vision_pro_assistant.trigger_gemini_vision_pro(image_path)

                elif "front of me" in voice_input:
                    webcam = WebcamCapture(voice_assistant)
                    image_path = webcam.capture_photo()
                    question = "Tell me about the picture in short"
                    gemini_vision_pro_assistant.trigger_gemini_vision_pro(image_path,question)

                elif 'alert' in [token.lemma_ for token in doc]:
                    notification.send_notification()

                elif 'message' in [token.lemma_ for token in doc]:
                    dba.sendMessage()

                elif 'currency' in [token.lemma_ for token in doc]:
                    webcam = WebcamCapture(voice_assistant)
                    image_path = webcam.capture_photo()
                    currency_detector.detect_currency(image_path)
                    
                elif 'navigate' in [token.lemma_ for token in doc]:
                    voice_assistant.speak("Tell me the destination")
                    route = voice_assistant.get_audio()
                    navigate.setupNavigation(route)
                    if "stop" in [token.lemma_ for token in doc]:
                         navigate.stopNavigation()
                
                elif "time" in [token.lemma_ for token in doc]:
                     datetime.get_time()
                     

                elif "date" in [token.lemma_ for token in doc]:
                     datetime.get_date()

                elif "call" in [token.lemma_ for token in doc]:
                     voice_assistant.speak("whom would you like to call")
                     name = voice_assistant.get_audio()
                     contact = dba.checkContacts(name)
                     if contact:
                         pi.callPhone(contact['phoneNumber'])

                elif "question" in [token.lemma_ for token in doc]:
                    question = voice_assistant.get_audio()
                    gemini_pro_assistant.respond(question)
        

def process2():
	while True:
		pi.getLocation()
		pi.listenGyro()
		navigate.navigate(pi.user_coord)
          

def process3():
     
    camera = cv2.VideoCapture(0)
    
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

        # Add the depth image over the color image:
        combinedImg = cv2.addWeighted(img, 0.7, colorDepth, 0.6, 0)

        # Join the input image, the estimated depth, and the combined image
        img_out = np.hstack((img, colorDepth, combinedImg))
        # cv2.putText(img_out, "FPS: {}".format(depthEstimator.fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img_out, "FPS: {}".format(fps), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 2)

        position = depthEstimator.checkDistanceThreshold(depth_map, img.shape[1])

        cv2.imshow("Depth Image", combinedImg)
        t2 = cv2.getTickCount()
        time1 = (t2-t1)/freq
        fps = 1/time1
        


        # Press key q to stop
        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def main():
    t2 = threading.Thread(target=process1)
    t1 = threading.Thread(target=process2)
    t3 = threading.Thread(target=process3)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    

if __name__ == "__main__":
    main()
   
	

	
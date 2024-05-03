import time
import spacy
import numpy as np
import threading
from server import FirebaseManager
from ocr import OCR
from piApi import piAPI
from capture import WebcamCapture
from voice import VoiceAssistant
from notification import NotificationSender
from stepBystep import NavigateUser
from dateandtime import DateAndTime
from gemini import GeminiVisionProAssistant,GeminiProAssistant
from events import Calendar
from inference import midasDepthEstimator
from objDetandGesRec.multimodal import *



json_file = "secret.json"
nlp = spacy.load('en_core_web_sm')

voice_assistant = VoiceAssistant()
stt = voice_assistant.selectModel()
is_offline = voice_assistant.is_system_offline()
dba = FirebaseManager(voice_assistant)
pi = piAPI(dba,voice_assistant)
navigate = NavigateUser(voice_assistant)
webcam = WebcamCapture(voice_assistant)
datetime = DateAndTime(voice_assistant)
gemini_pro_assistant = GeminiProAssistant(voice_assistant)
gemini_vision_pro_assistant = GeminiVisionProAssistant(voice_assistant)
ocr = OCR(voice_assistant)
notification = NotificationSender(voice_assistant)
event = Calendar(voice_assistant)
detection = Detector(voice_assistant)
video = VideoStream()



def process1():
    voice_assistant.speak("Listening")
    WAKE = "Sense"
    while True:
        voice_input = stt()
        print(voice_input)

        if voice_input == WAKE:
            voice_assistant.speak("Sixth Sense listening")

            while True:
                voice_input = stt()
                print(voice_input)
                doc = nlp(voice_input)

                if 'photo' in [token.lemma_ for token in doc]:
                    webcam = WebcamCapture(voice_assistant)
                    image_path = webcam.capture_photo()
                    voice_assistant.speak("What would you like to do")
                    question = stt()
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
                    voice_assistant.speak("Tell the message")
                    message = stt()
                    dba.sendMessage(message)
                    
                elif "what do i have" in voice_input.lower()  or ("create a event" in voice_input.lower() ) or ("make a note" in voice_input.lower() ):
                    event.find(voice_input.lower())

                # elif 'currency' in [token.lemma_ for token in doc]:
                #     webcam = WebcamCapture(voice_assistant)
                #     image_path = webcam.capture_photo()
                #     currency_detector.detect_currency(image_path)
                    
                elif 'navigate' in [token.lemma_ for token in doc]:
                    voice_assistant.speak("Tell me the destination")
                    route = stt()
                    navigate.setupNavigation('Mogappair erischeme')
                    if "stop" in [token.lemma_ for token in doc]:
                         navigate.stopNavigation()
                
                elif "time" in [token.lemma_ for token in doc]:
                     datetime.get_time()
                     
                elif "date" in [token.lemma_ for token in doc]:
                     datetime.get_date()

                elif "call" in [token.lemma_ for token in doc]:
                     voice_assistant.speak("whom would you like to call")
                     name = stt()
                     contact = dba.checkContacts(name)
                     if contact:
                         pi.callPhone(contact['phoneNumber'])
                         
                elif "question" in [token.lemma_ for token in doc]:
                #else:
                    voice_assistant.speak("yes sir")
                    question = stt()
                    if (is_offline):
                        response = ollama.chat(model='gemma:2b', messages=[
                                  {
                                    'role': 'user',
                                    'content': 'What do you mean by happy',
                                  }
                                ],  stream=False)
                        voice_assistant.speak(response['message']['content'])
                    else:
                        gemini_pro_assistant.respond(question)
        

def process2():
    while True:
        time.sleep(0.05)
        if (pi.GPSActive == True):
            pi.getLocation()
        pi.listenGyro()
        navigate.navigate(pi.user_coord)


def process3():
    depth_estimator = midasDepthEstimator(voice_assistant,pi)
    while True:
        depth_estimator.run(video.frame)
        

def process4():
    
    multimodal = multimodal_perception()
    while True:
        video.getFrame()
        multimodal.run(video.frame)





def main():
     t1 = threading.Thread(target=process1)
     t2 = threading.Thread(target=process2)
     t3 = threading.Thread(target=process3)
     t4 = threading.Thread(target=process4)
     t1.start()
     t2.start()
     t3.start()
     t4.start()
     t1.join()
     t2.join()
     t3.join()
     t4.join()
    

if __name__ == "__main__":
    main()
   
	

	

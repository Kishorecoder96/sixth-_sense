from faceEmotion import faceEmotion
from gesrec import HandGestureRecognition
from detection import Detector,argparse
from time import sleep
from voice_tts import VoiceAssistant
import cv2
from face_distance import FaceDetector
from currency import CurrencyRecognizer
from picamera2 import Picamera2
import time
import threading
import numpy as np
from main import midas

voice_assistant = VoiceAssistant()

class VideoStream():
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)},controls={"FrameRate": 8,"FrameDurationLimits": (40000, 40000)}))
        self.picam2.start()
        self.getFrame()
    
    def getFrame(self):
        self.frame = self.picam2.capture_array()
        return self.frame


class multimodal_perception():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--modeldir', help='Folder the .tflite file is located in', required=True)
        parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite', default='ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite')
        parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt', default='labelmap.txt')
        parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects', default=0.5)
        parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.', default='1280x720')
        parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection', action='store_true', default=True)
        args = parser.parse_args()
        self.mask = cv2.imread("mask.jpeg")
        self.hand_gesture_recognition = HandGestureRecognition(args)
        self.faceEmotion = faceEmotion(voice_assistant)
        self.currecyRecognition = CurrencyRecognizer(voice_assistant)
        self.feceDistance = FaceDetector(known_distance=30,known_width=5.7)
        self.detector = Detector(voice_assistant,args.modeldir, args.graph, args.labels, args.threshold, args.resolution, args.edgetpu)
        
    def run(self, frame1):
        frame = np.array(frame1)
        mask = cv2.resize(self.mask, (frame.shape[1], frame.shape[0]))
        imgRegion = cv2.bitwise_and(frame, mask)
        frame_rgb = cv2.cvtColor(imgRegion, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (self.detector.width, self.detector.height))
        
    
        hand, frame = self.hand_gesture_recognition.run(frame)
        self.faceEmotion.detect_faces(frame)
        self.currecyRecognition.predict(frame)
        if (hand == 1):
            boxes, classes, scores = self.detector.detect_objects(frame_resized)
               
            frame = self.detector.draw_boxes(frame, boxes, classes, scores)

   

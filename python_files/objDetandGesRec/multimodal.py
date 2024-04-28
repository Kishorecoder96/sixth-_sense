from faceEmotion import FaceEmotion
from gesrec import HandGestureRecognition
from detection import VideoStream,Detector,argparse
from time import sleep
from voice_tts import VoiceAssistant
import cv2

voice_assistant = VoiceAssistant()

videostream = VideoStream(framerate=30).start()
def multimodal_perception():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modeldir', help='Folder the .tflite file is located in', required=True)
    parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite', default='detect.tflite')
    parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt', default='labelmap.txt')
    parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects', default=0.5)
    parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.', default='1280x720')
    parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection', action='store_true')
    args = parser.parse_args()

    hand_gesture_recognition =HandGestureRecognition(args)
    faceEmotion = FaceEmotion(voice_assistant)
   
    detector = Detector(voice_assistant,args.modeldir, args.graph, args.labels, args.threshold, args.resolution, args.edgetpu)
    
    sleep(1)

    while True:
        frame1 = videostream.read()
        frame = frame1.copy()
        frame_rgb = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (detector.width, detector.height))
        
        hand, frame = hand_gesture_recognition.run(frame)
    
        faceEmotion.detect_faces(frame)

        if (hand == 1):
            boxes, classes, scores = detector.detect_objects(frame_resized)
           
            frame = detector.draw_boxes(frame, boxes, classes, scores)

        cv2.imshow('Multimodal Perception', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    videostream.stop()


if __name__ == "__main__":
    multimodal_perception()

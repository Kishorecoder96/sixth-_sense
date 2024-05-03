
import cv2

class FaceDetector:
    def __init__(self, known_distance, known_width):
       
        self.known_distance = known_distance
        self.known_width = known_width 

        self.green = (0, 255, 0)
        self.red = (0, 0, 255)
        self.black = (0, 0, 0)
        self.yellow = (0, 255, 255)
        self.white = (255, 255, 255)
        self.cyan = (255, 255, 0)
        self.magenta = (255, 0, 242)
        self.golden = (32, 218, 165)
        self.light_blue = (255, 9, 2)
        self.purple = (128, 0, 128)
        self.chocolate = (30, 105, 210)
        self.pink = (147, 20, 255)
        self.orange = (0, 69, 255)

        self.fonts = cv2.FONT_HERSHEY_COMPLEX
        self.fonts2 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        self.fonts3 = cv2.FONT_HERSHEY_COMPLEX_SMALL
        self.fonts4 = cv2.FONT_HERSHEY_TRIPLEX

        self.distance_level = 0

        self.face_detector = cv2.CascadeClassifier("model/faceEmoModel/haarcascade_frontalface_default.xml")

    def focal_length(self, measured_distance, real_width, width_in_rf_image):
       
        focal_length = (width_in_rf_image * measured_distance) / real_width
        return focal_length

    def distance_finder(self, focal_length, real_face_width, face_width_in_frame):
       
        distance = (real_face_width * focal_length) / face_width_in_frame
        return distance

    def face_data(self, image, call_out, distance_level):
    
        face_width = 0
        face_x, face_y = 0, 0
        face_center_x = 0
        face_center_y = 0
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray_image, 1.3, 5)
        for (x, y, w, h) in faces:
            line_thickness = 2
            llv = int(h * 0.12)

            face_width = w
            face_center_x = int(w / 2) + x
            face_center_y = int(h / 2) + y
            if distance_level < 10:
                distance_level = 10

        return face_width, faces, face_center_x, face_center_y

    def run(self,frame):
        # Reading reference image from directory
        ref_image = cv2.imread("ref_image.jpeg")
        ref_image_face_width, _, _, _ = self.face_data(ref_image, False, self.distance_level)
        focal_length_found = self.focal_length(self.known_distance, self.known_width, ref_image_face_width)

        face_width, faces, face_center_x, face_center_y = self.face_data(frame, True, self.distance_level)
        distance = self.distance_finder(focal_length_found, self.known_width, face_width)
        return distance



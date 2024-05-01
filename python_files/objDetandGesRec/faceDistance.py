
import cv2

class FaceDetector:
    def __init__(self, known_distance, known_width):
        # Variables
        self.known_distance = known_distance  # Inches
        self.known_width = known_width  # Inches

        # Colors (BGR Format)
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

        # Fonts
        self.fonts = cv2.FONT_HERSHEY_COMPLEX
        self.fonts2 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        self.fonts3 = cv2.FONT_HERSHEY_COMPLEX_SMALL
        self.fonts4 = cv2.FONT_HERSHEY_TRIPLEX

        # Camera Object
        self.distance_level = 0

        # Face Detector Object
        self.face_detector = cv2.CascadeClassifier("/Users/danny/Downloads/sixth-senseKish/python_files/objDetandGesRec/model/models/haarcascade_frontalface_default.xml")

    def focal_length(self, measured_distance, real_width, width_in_rf_image):
        """
        This Function Calculate the Focal Length(distance between lens to CMOS sensor), it is simple constant we can find by using
        MEASURED_DISTACE, REAL_WIDTH(Actual width of object) and WIDTH_OF_OBJECT_IN_IMAGE
        :param1 Measure_Distance(int): It is distance measured from object to the Camera while Capturing Reference image
        :param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 5.7 Inches)
        :param3 Width_In_Image(int): It is object width in the frame /image in our case in the reference image(found by Face detector)
        :retrun Focal_Length(Float):
        """
        focal_length = (width_in_rf_image * measured_distance) / real_width
        return focal_length

    def distance_finder(self, focal_length, real_face_width, face_width_in_frame):
        """
        This Function simply Estimates the distance between object and camera using arguments(Focal_Length, Actual_object_width, Object_width_in_the_image)
        :param1 Focal_length(float): return by the Focal_Length_Finder function
        :param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 5.7 Inches)
        :param3 object_Width_Frame(int): width of object in the image(frame in our case, using Video feed)
        :return Distance(float) : distance Estimated
        """
        distance = (real_face_width * focal_length) / face_width_in_frame
        return distance

    def face_data(self, image, call_out, distance_level):
        """
        This function Detect face and Draw Rectangle and display the distance over Screen
        :param1 Image(Mat): simply the frame
        :param2 Call_Out(bool): If want show Distance and Rectangle on the Screen or not
        :param3 Distance_Level(int): which change the line according the Distance changes(Intractivate)
        :return1  face_width(int): it is width of face in the frame which allow us to calculate the distance and find focal length
        :return2 face(list): length of face and (face paramters)
        :return3 face_center_x: face centroid_x coordinate(x)
        :return4 face_center_y: face centroid_y coordinate(y)
        """
        face_width = 0
        face_x, face_y = 0, 0
        face_center_x = 0
        face_center_y = 0
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray_image, 1.3, 5)
        for (x, y, w, h) in faces:
            line_thickness = 2
            llv = int(h * 0.12)

            cv2.line(image, (x, y + llv), (x + w, y + llv), (self.green), line_thickness)
            cv2.line(image, (x, y + h), (x + w, y + h), (self.green), line_thickness)
            cv2.line(image, (x, y + llv), (x, y + llv + llv), (self.green), line_thickness)
            cv2.line(image, (x + w, y + llv), (x + w, y + llv + llv), (self.green), line_thickness)
            cv2.line(image, (x, y + h), (x, y + h - llv), (self.green), line_thickness)
            cv2.line(image, (x + w, y + h), (x + w, y + h - llv), (self.green), line_thickness)

            face_width = w
            face_center_x = int(w / 2) + x
            face_center_y = int(h / 2) + y
            if distance_level < 10:
                distance_level = 10

        return face_width, faces, face_center_x, face_center_y

    def run(self,frame):
        # Reading reference image from directory
        ref_image = cv2.imread("/Users/danny/Downloads/sixth-senseKish/python_files/objDetandGesRec/ref_image.jpeg")
        ref_image_face_width, _, _, _ = self.face_data(ref_image, False, self.distance_level)
        focal_length_found = self.focal_length(self.known_distance, self.known_width, ref_image_face_width)

        face_width, faces, face_center_x, face_center_y = self.face_data(frame, True, self.distance_level)
        distance = self.distance_finder(focal_length_found, self.known_width, face_width)
        return distance


# if __name__ == "__main__":
#     fd = FaceDetector(known_distance=30, known_width=5.7)
#     fd.run()
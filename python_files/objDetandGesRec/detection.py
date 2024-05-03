import os
import argparse
import cv2
import numpy as np
from threading import Thread
import threading
import importlib.util
from time import sleep, time
import tensorflow as tf


class Detector:
    def __init__(self,voice_assistant, modeldir,graph='detect_edgetpu.tflite', labels='labelmap.txt', threshold=0.5, resolution='1280x720', edgetpu=False):
        self.MODEL_NAME = modeldir
        self.GRAPH_NAME = graph
        self.voice_assistant = voice_assistant
        self.LABELMAP_NAME = labels
        self.found_name = None
        self.found_objects = []
        self.min_conf_threshold = float(threshold)
        resW, resH = resolution.split('x')
        self.imW, self.imH = int(resW), int(resH)
        self.use_TPU = edgetpu
        
        pkg = importlib.util.find_spec('tflite_runtime')
        if pkg:
            from tflite_runtime.interpreter import Interpreter
            if self.use_TPU:
                from tflite_runtime.interpreter import load_delegate
        else:
            from tf.lite.python.interpreter import Interpreter
            if self.use_TPU:
                from tf.lite.python.interpreter import load_delegate

        CWD_PATH = os.getcwd()
        self.PATH_TO_CKPT = os.path.join(CWD_PATH, self.MODEL_NAME, self.GRAPH_NAME)
        self.PATH_TO_LABELS = os.path.join(CWD_PATH, self.MODEL_NAME, self.LABELMAP_NAME)

        with open(self.PATH_TO_LABELS, 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]

        if self.labels[0] == '???':
            del self.labels[0]

        if self.use_TPU:
            self.interpreter = Interpreter(model_path=self.PATH_TO_CKPT, experimental_delegates=[load_delegate('libedgetpu.so.1.0')])
        else:
            self.interpreter = Interpreter(model_path=self.PATH_TO_CKPT)

        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]
        self.floating_model = (self.input_details[0]['dtype'] == np.float32)
        self.input_mean = 127.5
        self.input_std = 127.5
        self.outname = self.output_details[0]['name']
        if ('StatefulPartitionedCall' in self.outname):
            self.boxes_idx, self.classes_idx, self.scores_idx = 1, 3, 0
        else:
            self.boxes_idx, self.classes_idx, self.scores_idx = 0, 1, 2

    def detect_objects(self, frame_resized):
        input_data = np.expand_dims(frame_resized, axis=0)
        if self.floating_model:
            input_data = (np.float32(input_data) - self.input_mean) / self.input_std
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        boxes = self.interpreter.get_tensor(self.output_details[self.boxes_idx]['index'])[0]
        classes = self.interpreter.get_tensor(self.output_details[self.classes_idx]['index'])[0]
        scores = self.interpreter.get_tensor(self.output_details[self.scores_idx]['index'])[0]
        return boxes, classes, scores

    def draw_boxes(self, frame, boxes, classes, scores):
        for i in range(len(scores)):
            if ((scores[i] > self.min_conf_threshold) and (scores[i] <= 1.0)):
                ymin = int(max(1, (boxes[i][0] * self.imH)))
                xmin = int(max(1, (boxes[i][1] * self.imW)))
                ymax = int(min(self.imH, (boxes[i][2] * self.imH)))
                xmax = int(min(self.imW, (boxes[i][3] * self.imW)))
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (10, 255, 0), 2)
                object_name = self.labels[int(classes[i])]
                label = '%s' % (object_name)
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                label_ymin = max(ymin, labelSize[1] + 10)

                if (scores[i] * 100) > 65:

                    if len(self.found_objects) > 3:
                        self.found_objects = []
                    if label in self.found_objects:
                        continue
                    else:
                        self.found_objects.append(label)
                        self.voice_assistant.speak(label)
                   
                
        return frame

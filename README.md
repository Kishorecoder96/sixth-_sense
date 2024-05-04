<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Sixth Sense](#sixth-sense)
  - [**Architecture**:](#architecture)
    - [**Old Architecture**](#old-architecture)
    - [**New Architecture**](#new-architecture)
    - [Technology Arsenal:](#technology-arsenal)
  - [1 Machine Learning:](#1-machine-learning)
    - [1.1 Optical character Recognition(OCR):](#11-optical-character-recognitionocr)
    - [1.2 Natural Language Processing using Spacy:](#12-natural-language-processing-using-spacy)
    - [Voice Assistant:](#voice-assistant)
      - [1.3 Speech To Text:](#13-speech-to-text)
      - [1.4 Text To Speech](#14-text-to-speech)
    - [1.5 Distance Warning System](#15-distance-warning-system)
    - [1.6 Voice Enabled Calendar Management](#16-voice-enabled-calendar-management)
    - [1.7 Gemini and gemma](#17-gemini-and-gemma)
    - [Emotional Detection,Face Recognition and Distance Measurement](#emotional-detectionface-recognition-and-distance-measurement)
      - [1.8 Emotional Detection:](#18-emotional-detection)
      - [1.9 Face Recognition](#19-face-recognition)
      - [1.10 Face Distance Calculation](#110-face-distance-calculation)
    - [Object Detection and Gesture Recognition:](#object-detection-and-gesture-recognition)
      - [1.11 Gesture Recognition:](#111-gesture-recognition)
      - [1.12 Object Detection:](#112-object-detection)
    - [1.13 Currency Recognition](#113-currency-recognition)
  - [2 Software](#2-software)
    - [2.1 Geofencing](#21-geofencing)
    - [2.2 Messaging](#22-messaging)
    - [2.3 Multi Language Support](#23-multi-language-support)
    - [2.4 Contact](#24-contact)
  - [3 Hardware](#3-hardware)
    - [Hardware Architecture:](#hardware-architecture)
    - [3.1 Fall Detection](#31-fall-detection)
    - [3.2 **Vibration Motor: Enhancing Safety Measures**](#32-vibration-motor-enhancing-safety-measures)
    - [3.3 TPU (Tensor Processing Unit)](#33-tpu-tensor-processing-unit)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# Sixth Sense

<div style="text-align: center;">
    <img src="https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/logo.png" alt="logo" style="width: 100px; height: 100px;">
</div>

![sixth sense](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/Frame%20179.png)
 **Generations**:


## Executing the Code:
  ####  For Software:
  1. Download the library and run the code:
   ```bash
        npm install
        npm start
   ```
#### For Machine Learning:
1. Create a new conda environment named sense by running:
```bash
conda create -n sense python=3.11
```
2. Activate the environment:
```bash
conda activate sense
```
3. To install the requirements:
```bash
pip install -r requirements.txt
```
 4.To run the file:
```
python main.py —modeldir objDetandGesRec/model/custom_mo
```
## **Architecture**:
    
### **Old Architecture**
![Old Archictecture](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/Old%20architecture%20(2).png)
### **New Architecture**
![New Architecture](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/overallArchitecture-background.png)
### Features
![features](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/Features.png)
### Technology Arsenal:


#### Google Products

1. **Firebase** <img width="30" height="20" src="https://img.icons8.com/color/48/firebase.png" alt="firebase">
   - **Infrastructure and Security:** Provides a reliable and scalable backend with built-in security features for data management and user authentication.

2. **Google Maps API** <img width="30" height="20" src="https://img.icons8.com/color/48/google-maps-new.png" alt="google-maps-new">
   - **Directions API:** Integrates reliable navigation information from Google Maps for safe and efficient travel planning.

3. **Google Calendar API** <img width="30" height="20" src="https://img.icons8.com/color/48/google-calendar--v2.png" alt="google-calendar--v2">
   - **Virtual Assistant Functionalities:** Provides virtual assistant functionalities, including accessing calendar events and creating notes using speech recognition and text-to-speech.

4. **Gemini**
   - **Personal Companion:** Core intelligence system offering environmental awareness, navigation, alerts, and voice messaging for personalized assistance.

5. **Coral TPU** <img width="30" height="20" src="https://img.icons8.com/office/30/coral.png" alt="coral">
   - **Accelerated Machine Learning:** Integrates Coral TPU for accelerated machine learning tasks, enhancing performance and efficiency.

6. **TensorFlow Lite**
   - **Lightweight Machine Learning:** Utilizes TensorFlow Lite for deploying machine learning models on resource-constrained devices, optimizing performance on edge devices.

7. **MediaPipe**
   - **Real-time Hand Tracking and Gesture Recognition:** Chosen for its real-time hand tracking and gesture recognition capabilities, allowing the device to understand hand movements and translate them into action.

8. **Google Speech-To-Text** <img width="30" height="20" src="https://img.icons8.com/ios-glyphs/30/speech-to-text.png" alt="speech-to-text">
   - **Real-time Speech-to-Text Conversion:** Converts speech to text for situations where an internet connection allows real-time processing for greater accuracy and features.

#### Other Technologies

9. **React Native** <img width="30" height="20" src="https://img.icons8.com/officel/30/react.png" alt="react">
   - **App for Caretaker:** Cross-platform mobile application framework ensuring a consistent user experience across different devices and operating systems.

10. **Pi OS** <img width="30" height="20" src="https://img.icons8.com/color/48/raspberry.png" alt="raspberry">
    - **Lightweight and Automation:** Optimized operating system for Raspberry Pi devices, conserving resources and enabling automation tasks.

11. **OpenCV** <img width="30" height="20" src="https://img.icons8.com/color/48/opencv.png" alt="opencv">
    - **Face Recognition:** Utilized for facial recognition functionalities to enhance security and provide personalized assistance.

12. **Torch**
    - **Speech to Text:** Enables voice command interaction through speech-to-text conversion, enhancing accessibility and user experience.

13. **OCR** <img width="30" height="20" src="https://img.icons8.com/material/24/printed-ocr.png" alt="printed-ocr">
    - **Extracting Images:** Extracts text from images to improve comprehension and facilitate data processing.

14. **Whisper Speech-To-Text** <img width="30" height="20" src="https://img.icons8.com/ios-filled/50/whisper.png" alt="whisper">
    - **Offline Speech Recognition:** Employed for real-time speech-to-text conversion without an internet connection.

15. **pyttsx3**
    - **Text to Speech Conversion:** Converts text to speech on the device itself, providing voice feedback without an internet connection.

16. **langchain**
    - **Optimizing Communication:** Acts as a bridge, refining questions and requests for optimal understanding by the large language model.

17. **Face-Recognition** <img width="30" height="20" src="https://img.icons8.com/external-flat-circular-vectorslab/68/external-Face-Recognition-interior-flat-circular-vectorslab.png" alt="external-Face-Recognition-interior-flat-circular-vectorslab">
    - **Visual Identification:** Recognizes faces, helping visually impaired individuals to identify people.

18. **pyaudio**
    - **Microphone Interface:** Captures spoken words for the device to understand.

19. **geopy**
    - **Location-Based Services:** Calculates distances between locations based on their coordinates.

20. **easyocr**
    - **Text Recognition:** Empowers the device to "read" text, converting images of characters to digital text.


## 1 Machine Learning:
## 1.1 Optical character Recognition(OCR):
 Introduction

We have integrated optical character recognition (OCR) technology into our system to support visually impaired individuals in accessing textual content from images. This advancement enables users to hear the text embedded within images, thereby enhancing accessibility and fostering greater independence in navigating printed materials. By harnessing OCR capabilities, our solution empowers visually impaired individuals to convert visual information into audible text, facilitating easier comprehension and engagement with written content.

 Requirements

- easyocr
- pillow
- cv2

 Working Flow of Optical Character Recognition

1. **Initialization:**
    - The OCR class initializes with a voice_assistant object, language settings (defaulted to English and Hindi), and an option to use GPU for processing.
    - An instance of the easyocr.Reader class is created within the constructor, configured with specified languages and GPU usage.
2. **Text Extraction from Image:**
    - The extract_text_from_image method processes an image file path.
    - It uses OpenCV to read the image and standardizes its dimensions to 800x600 pixels for consistency.
    - easyocr.Reader's readtext method is invoked to extract text from the resized image, returning a list of tuples with text content and other details.
    - Extracted text is concatenated into a single string.
    - If text is detected (length of concatenated text > 0), the voice_assistant object vocalizes the text.
    - In absence of detected text, the voice assistant communicates a default message indicating inability to provide an answer.
 ### 1.2 Natural Language Processing using Spacy:
Introduction

We have leveraged the power of spaCy, a natural language processing (NLP) library, to enhance accessibility for visually impaired individuals. By integrating spaCy into our system, we have enabled intuitive interaction through voice commands, allowing users to effortlessly communicate and engage with the system's functionalities. SpaCy's robust NLP capabilities enable us to interpret and understand spoken commands, empowering visually impaired individuals to perform a variety of tasks efficiently and independently. Through tokenization, part-of-speech tagging, named entity recognition, and dependency parsing, spaCy enables us to analyze and process textual data derived from voice input, facilitating seamless communication and interaction with the assistive technology. This integration not only improves accessibility but also fosters greater independence and inclusivity for visually impaired individuals in navigating and accessing information in the digital realm.

 Requirements

- spacy
- en_core_web_sm

 Workflow of Spacy

- **Initialization**:
    - The spaCy model for English language processing (**`en_core_web_sm`**) is loaded.
- **Command Interpretation**:
    - The user's voice input (**`voice_input`**) is processed using spaCy's NLP capabilities.
    - Lemmatized tokens are extracted from the processed text to identify key actions or entities mentioned by the user.
    - If specific keywords or phrases indicative of different actions are identified, corresponding tasks are executed accordingly.
- **Conditional Execution of Tasks**:
    - Based on the identified actions or entities, conditional statements are used to trigger specific functions or processes.
    - For example, if the command contains the word "photo," the system initiates photo capture using the webcam. If the word "text" is detected in conjunction with "photo," text extraction from the captured image is performed using an Optical Character Recognition (OCR) tool.
    - Similarly, other actions such as sending notifications, sending messages, detecting currency, navigating, retrieving time or date, making calls, creating events, and taking notes are executed based on the identified keywords.
## Voice Assistant:
![voice assistant](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/speech-speech-background.png)
### 1.3 Speech To Text:

 **Introduction**

We have built a speech-to-text system tailored for individuals with visual impairments. Our system seamlessly integrates with Google's powerful speech recognition technology, allowing users to convert spoken words into text format. This innovation aims to enhance accessibility and independence for visually impaired individuals in their daily lives. With a focus on online connectivity, our system ensures access to Google's speech-to-text service whenever network connectivity is available. However, we understand that internet connectivity may not always be reliable. In such cases, our system seamlessly switches to a whisper tiny offline model, ensuring uninterrupted assistance for visually impaired individuals, regardless of internet availability.

 Requirements

- Speech Recognition
- PlaySound
- torch
- whisper

 Working Flow of Google Speech To Text

1. **Initialization:**
    - The project initializes and sets up necessary components, including importing required libraries and setting up any configurations.

1. **Audio Input:**
    - The program captures audio input from the user, typically through a microphone connected to the device.
2. **Speech Recognition:**
    - The captured audio data is sent to Google's speech-to-text service for recognition.
3. **Processing:**
    - Google's service processes the audio data and converts it into text, using advanced algorithms and models.
4. **Transcription:**
    - The recognized text output is returned by Google's service and received by the program.

 Working Flow of Whisper Speech To Text

1. **Initialization:**
    - The program starts by parsing command-line arguments using **`argparse`**. These arguments define various parameters such as the model to use, energy threshold for the microphone, and timeouts for recording.
    - It initializes necessary components like a thread-safe queue for passing audio data, a speech recognizer, and the microphone source.
2. **Audio Input:**
    - The program sets up the microphone source, adjusting for ambient noise using **`recorder.adjust_for_ambient_noise()`**.
3. **Speech Recognition:**
    - It loads or downloads the specified model using the **`whisper.load_model()`** function.
    - If running on Linux, it checks for available microphones and selects the one specified in the command-line arguments.
4. **Processing:**
    - The program sets up a background thread to continuously capture audio data using **`recorder.listen_in_background()`**.
    - It converts the raw audio data into a format compatible with the speech recognition model and performs transcription using **`audio_model.transcribe()`**.
5. **Transcription:**
    - As audio data is received, it's processed and transcribed in real-time.
    - The transcription is updated and printed to the console, clearing the console to display the latest transcription.

 Challenges

1. We encountered challenges while integrating the speech-to-text functionality with our Raspberry Pi. These challenges manifested as errors related to the Jack server not being found and the ALSA card not being detected. Surprisingly, these errors did not occur when running the code individually. However, when attempting to execute the code within another file, a segmentation error occurred, preventing successful execution.|

**Solution:** After extensive investigation and troubleshooting efforts, we discovered that downloading and installing additional files resolved the issues we were encountering. This solution enabled us to overcome the segmentation error and successfully integrate the speech-to-text functionality with our Raspberry Pi setup.
2. We encountered challenges in providing audio input to the model for triggering functions, primarily due to the continuous listening nature of the speech recognition model. This posed difficulties as our intended functions required specific audio cues to activate. Despite these challenges, we found a solution that allowed us to make it work correctly. 

S**olution:** Through diligent experimentation and refinement, we were able to implement a method that effectively synchronized the audio input with the desired function triggers, enabling smooth and accurate operation of the system.

### 1.4 Text To Speech

 Introduction

We've developed a robust text-to-speech solution utilizing pyttsx3, tailored to aid visually impaired individuals in accessing device outputs audibly. This innovation empowers users to hear device-generated text, enhancing accessibility and promoting independence in engaging with digital content.

 Requirement

- pyttsx3
-  Working Flow of Text To Speech

1. **Initialization:** To use pyttsx3, you first initialize an instance of the text-to-speech engine using the **`pyttsx3.init()`** method. This initializes the TTS engine with default settings.
2. **Configuration:** After initialization, you can configure various properties of the TTS engine using methods like **`setProperty()`**. Properties such as speech rate, volume, and voice selection can be adjusted according to preference.
3. **Speech Synthesis:** Once the engine is initialized and configured, you can use the **`say()`** method to input text that you want to be converted into speech. This method queues the text for speech synthesis.
4. **Speech Rendering:** The TTS engine processes the queued text and synthesizes it into audible speech using text-to-speech synthesis algorithms.
5. **Playback:** After the speech synthesis is completed, the generated speech is played back through the device's speakers or audio output.
6. **Synchronous Operation:** By default, pyttsx3 operates synchronously, meaning that the **`say()`** method blocks until the entire text is spoken. This ensures that the speech is completed before the program proceeds to the next line of code.

###  1.5 Distance Warning System

 Introduction

We have implemented a  distance warning system designed to assist visually impaired individuals in navigating their surroundings safely. Leveraging the advanced depth estimation capabilities of MidasV2 with a single camera setup, our system accurately calculates distances between the user and surrounding obstacles in real-time. With prompt audible alerts generated upon detecting obstacles within a customizable threshold distance, our system ensures timely warnings to prevent potential collisions. Additionally, incorporating an offline model guarantees uninterrupted assistance even in areas with limited internet connectivity, enhancing accessibility and independence for visually impaired individuals.
![Distance](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/navigation2.png)
 Requirements

- numpy
- openCv
- midasmodel_edgetpu.tflite
- pyttsx3

 Workingflow of Distance Warning using Depth Estimation

**Initialization:**

- In this phase, the necessary components for the operation of the code are initialized. This includes:
    - Instantiating the **`VoiceAssistant`** and **`midasDepthEstimator`** classes, which are essential for providing auditory feedback and performing depth estimation, respectively.

**Model Initialization:**

- Within the **`midasDepthEstimator`** class, the MidasV2 depth estimation model is initialized. This involves:
    - Loading the pre-trained MidasV2 model from a specified path.
    - Allocating resources for inference, such as memory space for model parameters and input/output tensors.

**Webcam Initialization:**

- The code initializes the webcam using OpenCV's **`VideoCapture`** function. This step allows the code to:
    - Establish a connection with the webcam hardware.
    - Access the video stream for capturing live frames.

**Main Loop:**

- The main loop serves as the core of the program, orchestrating the sequence of operations for each iteration. It includes the following steps:

**Frame Acquisition:**

- Within the loop, frames are continuously captured from the webcam using the **`camera.read()`** function. This involves:
    - Retrieving the next frame from the webcam.
    - Storing the frame as an image for further processing.

**Depth Estimation:**

- The captured frame undergoes depth estimation using the MidasV2 model within the **`midasDepthEstimator`** class. This process includes:
    - Preprocessing the image to prepare it for input to the model.
    - Performing inference with the MidasV2 model to estimate depth.
    - Post-processing the output to generate a depth map representing the relative distances of objects in the scene.

**Distance Threshold Check:**

- After obtaining the depth map, the code analyzes it to check for objects within a predefined distance threshold. This involves:
    - Converting the depth map into meters to obtain real-world distances.
    - Comparing the minimum depth value against a predefined threshold distance to determine if an object is too close to the camera.
    - Issuing a warning via the **`VoiceAssistant`** if an object is detected within the threshold distance.
    
     Challenges
    
    The primary difficulty stemmed from the constraint of not using sensors like LiDAR or ultrasonic devices. Instead, we opted to develop a warning system solely relying on a single camera. This decision posed several technical hurdles and complexities in determining how to effectively execute the functionality of the system.
    
    **Solution:**
    
    To address the challenge of developing a warning system without the use of sensors, we devised a novel approach based on depth estimation techniques. By analyzing the depth of objects within the image, we were able to determine the overall depth of the scene. This depth information enabled us to implement a threshold value, beyond which warnings would be triggered to alert the user of potential obstacles.
    
    Moreover, to enhance the warning system's effectiveness, we implemented a side warning feature. If the minimum depth detected fell below the threshold, the system would assess the object's position within the scene. If the object was on the left side, the system would advise the user to move right through text-to-speech output. Similarly, if the object was on the right side, the system would recommend moving left. This side-specific warning mechanism provided users with precise guidance on how to navigate around obstacles, further improving the system's utility and user experience.
  
### 1.6 Voice Enabled Calendar Management
Introduction

We have integrated Google Calendar API in our Sixth Sense to provide vital resources for visually impaired individuals, enabling them to manage schedules and tasks effortlessly through voice commands. With the ability to create events on specific days and inquire about their schedule for any given day, users gain instant access to crucial information, enhancing their organization and time management skills. Additionally, the feature allowing users to make notes by simply dictating them aloud offers a convenient way to capture important thoughts and reminders.

Moreover, our solution incorporates speech-to-text functionality, ensuring seamless interaction for users. When online connectivity is established, Google Speech Recognition is activated, allowing for accurate transcription of spoken commands. However, in cases where online connectivity fails, our system seamlessly switches to Whisper Tiny, ensuring uninterrupted assistance for visually impaired individuals. Through seamless integration with text-to-speech functionality using pyttsx3, our solution ensures accessibility, allowing visually impaired individuals to interact effectively with the system and lead more independent and productive lives.

 Requirements

- datetime
- pyttsx3
- Speech Recognition
- PlaySound
- torch
- whisper
- credentials.json
- notepad.exe

 Workflow of Calendar Management

1. **Authentication and Setup**:
    - The script begins by authenticating with the Google Calendar API using OAuth 2.0, allowing access to calendar data.
    - Necessary libraries and dependencies are imported, including Google Calendar API, text-to-speech (TTS) with `pyttsx3`, and speech recognition with `speech_recognition`.
    - Constants such as scopes, months, days, and day extensions are defined to aid in date recognition and event creation.
2. **Speech Recognition**:
    - The script listens for voice commands using the `speech_recognition` library, capturing user requests for calendar-related actions.
3. **Request Interpretation**:
    - User requests are analyzed to determine the desired action, such as querying upcoming events, creating a new event, or making a note.
    - Specific phrases are recognized to trigger corresponding actions, such as "what do I have" for checking upcoming events and "create an event" for event creation.
4. **Date Parsing**:
    - If the user requests information about a specific date, the script parses the user's speech to extract the relevant date information.
    - Date parsing involves identifying keywords such as days of the week, months, or specific phrases like "today" or "tomorrow" to determine the intended date.
5. **Calendar Interaction**:
    - Once the user's request and date are identified, the script interacts with the Google Calendar API to retrieve relevant calendar data.
    - For queries about upcoming events, the script fetches event details for the specified date range and provides auditory feedback to the user, announcing the events.
    - In the case of event creation requests, the script prompts the user for event details such as the event name and date. It then creates the event on the user's calendar via the Google Calendar API.
6. **Note Taking**:
    - If the user requests to make a note, the script records the spoken text and saves it as a note in a text file for future reference.
    - The note-taking functionality enhances the user's ability to quickly capture thoughts or reminders using voice commands, improving productivity and organization.
7. **Voice Feedback**:
    - Throughout the process, the script provides auditory feedback to the user using text-to-speech (TTS) technology (`pyttsx3`), ensuring a seamless and accessible user experience.
    - Auditory feedback includes confirmation messages, event details, and note-taking acknowledgments, enabling visually impaired users to interact effectively with the system.

By combining speech recognition, calendar API interaction, and voice feedback mechanisms, the code streamlines calendar management tasks for visually impaired individuals, offering enhanced accessibility and independence in organizing their schedules.

### 1.7 Gemini and gemma
Introduction

Our project integrates two powerful models, **Gemini** and **Gemma**, to provide assistance to visually impaired individuals. When online connectivity is available, Gemini is initiated to answer questions and provide information effectively. However, in situations where online connectivity is not established, Gemma seamlessly takes over to ensure uninterrupted assistance. This dynamic integration ensures continuous support for visually impaired individuals, regardless of their internet connection status. Additionally, our solution incorporates **Gemini Vision**, enabling users to explore their environment effectively. With Gemini Vision, users can inquire about objects or obstacles in front of them simply by asking questions. Furthermore, users have the ability to take a photo of their surroundings and ask questions about the captured image, enhancing their understanding and interaction with the world around them. This comprehensive approach to accessibility aims to empower visually challenged individuals by providing them with tools to access information, navigate their environment, and interact with their surroundings confidently and independently.
![](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/GemmaAndGemini-background.png)
 Requirements

- langchain
- google.generativeai
- pillow
- langchain_google_genai
- ollama

 Workflow of Gemini and Gemma

 **System Connectivity Status**

- `is_system_offline` method crucial for determining system's online status.
- It attempts socket connection to a well-known external server like Google DNS.
- Uses `create_connection` function from `socket` module.
- Connection made with server IP "8.8.8.8" and port 53.
- If successful, returns `False`, affirming online status.
- If connection fails (e.g., network issues), catches `OSError` and returns `True`, indicating offline status.
- Provides robust means to assess connectivity vital for network-dependent applications.
- Offers straightforward mechanism to ascertain online/offline status.
- Enables applications to adapt based on connectivity, ensuring optimal performance in diverse network environments.

```python
def is_system_offline(self):
        try:
            # Attempt to create a socket connection to a known external server (Google DNS).
            socket.create_connection(("8.8.8.8", 53))
            return False
        except OSError:
            return True
```

 **Adaptive Assistance for Online Connectivity**

- If `is_system_offline` evaluates to `False`, indicating that the system is online, the Gemini and GeminiVisionProAssistant classes are initiated to provide assistance to visually impaired users.
- The GeminiProAssistant class utilizes the LangChain Google Generative AI API to respond to user queries by triggering the Gemini model.
- With online connectivity established, the Gemini model generates concise responses based on user queries, extracting the first four words for clarity, which are then relayed to the user through the voice assistant.
- The GeminiVisionProAssistant class offers image description capabilities for visually impaired users, generating concise descriptions of images when triggered with an image file path.
- Similar to the GeminiProAssistant, if an internet connection is available, the Gemini Pro Vision model is invoked to analyze images and provide descriptive responses relayed to the user through the voice assistant.
- Robust error handling mechanisms ensure that any unforeseen issues are appropriately managed, with the voice assistant communicating any encountered errors.
- These integrated functionalities aim to empower visually impaired individuals by providing accurate and concise information through text and image-based interactions, enhancing accessibility and independence in daily tasks and information retrieval.
- Additionally, the input is acquired through speech to text using Google's speech recognition, and the output is spoken out with pyttsx3, ensuring seamless interaction and accessibility for visually impaired users.

 **Seamless Interaction in Offline Mode**

- When `is_system_offline` is `True`, indicating offline status, the Ollama model on Raspberry Pi 5 operates independently.
- The interaction begins with a user question, triggering the Ollama model.
- Tiny Whisper speech recognition converts the spoken query into text.
- The Ollama model processes the text input, formulating a response internally.
- The response is converted into speech using pyttsx3.
- The Raspberry Pi 5 device serves as the platform for hosting and executing the Ollama model.
- Seamless offline interaction is ensured, with responses conveyed through the device's audio output.

### Emotional Detection,Face Recognition and Distance Measurement
![archi](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/emotionAndFace-background.png)
   #### 1.8 Emotional Detection:
   

 Introduction

In this system, we integrate emotion detection technology with facial recognition to assist visually impaired individuals in perceiving the emotions of people around them. When a known person stands in front of a blind individual, our system utilizes a camera feed to recognize their facial expressions. This recognition process is initiated only when the system identifies a familiar face. Once a face is detected and identified, our technology analyzes the facial expression using advanced emotion detection algorithms. Subsequently, the system converts this emotional insight into spoken words through a speech synthesis engine, enabling the blind individual to understand the emotional state of the person in front of them. Through this innovative integration of technology, we aim to enhance the social interactions and situational awareness of visually impaired individuals, fostering a more inclusive and connected environment.
 Requirements

- openCv
- numpy
- face recognition
- tensorflow
- pyttsx3
- haarcascade_frontalface_default.xml
- modelemotion_edgetpu.tflite

 Workflow of Emotion Detection

1. **Initialization**:
    - Instantiate the **`FaceEmotion`** class with a **`voice_assistant`** object.
    - Load the emotion detection model (**`modelemotion.tflite`**) into the TensorFlow Lite interpreter.
    - Load known face encodings and names from the **`faces/`** directory.
    - Define a list of emotions corresponding to different facial expressions.
2. **Face Detection and Emotion Recognition Loop**:
    - Capture a frame from the camera feed.
    - Use the Haar cascade classifier to detect faces in the frame.
    - For each detected face:
        - Crop the face region.
        - Preprocess the face image.
        - Utilize the TensorFlow Lite model to recognize emotions from the preprocessed face image.
        - Display rectangles around detected faces and show the recognized emotion as text.
        - Conduct face recognition using the **`face_recognition`** library:
            - Compute face encodings for faces in the frame.
            - Compare face encodings with known face encodings.
            - If a match is found, display the name of the recognized person.
        - Provide verbal feedback using the voice assistant, announcing the recognized person's name and detected emotion.
3. **Preprocessing and Model Inference**:
    - Preprocess the input frame to fit the model input size (resize to 64x64 pixels, normalization).
    - Prepare the preprocessed frame for inference by converting it to the required format.
4. **Return Processed Frame**:
    - Return the processed frame with visual annotations (rectangles, text labels) indicating emotions and recognized faces.
5. **Loop Over Frames**:
    - Continuously repeat the face detection and emotion recognition process for each frame captured from the camera feed.
.
#### 1.9 Face Recognition
 Introduction

We've engineered a face recognition system designed to enhance their social interactions and overall sense of autonomy. This innovative technology represents a significant leap forward in accessibility, enabling blind individuals to discern and recognize the faces of those in their immediate vicinity. By harnessing the power of artificial intelligence and computer vision, our system provides invaluable assistance to individuals who rely on auditory cues to navigate the world around them.

 Requirements

- OpenCV
- haarcascade_frontalface_default.xml
- pyttsx3

 Workflow of FaceRecognition

1. **Initialization**:
    - The **`FaceEmotion`** class initializes with a **`voice_assistant`** parameter, presumably for some voice interaction capability.
    - It loads a TensorFlow Lite interpreter with a pre-trained emotion detection model (**`modelemotion.tflite`**).
    - Known face encodings and names are loaded from images in the 'faces/' directory using the face_recognition library.
2. **Image Preprocessing**:
    - The **`preprocess_img`** method resizes and normalizes input images to prepare them for inference.
3. **Emotion Detection**:
    - The **`brain`** method takes a cropped face image, preprocesses it, feeds it to the TensorFlow Lite model, and returns the predicted emotion.
    - The model used for emotion detection is a classifier that identifies emotions like anger, disgust, fear, etc.
4. **Face Detection**:
    - The **`detect_faces`** method takes a frame from the camera feed and detects faces using OpenCV's Haar Cascade classifier.
    - For each detected face, it performs emotion detection using the **`brain`** method and draws bounding boxes around the faces with the predicted emotion labels.
    - It also recognizes known faces by comparing their encodings with the encodings of detected faces using the face_recognition library.
5. **Face Recognition**:
    - Known faces are recognized using the face_recognition library by comparing face encodings.
    - If a known face is detected, its name is associated with the face.
#### 1.10 Face Distance Calculation

 Introduction

We've developed a Face Distance System. By seamlessly integrating  face detection technology into our solution, we've created a transformative experience that empowers individuals with visual challenges. This system intelligently activates when someone approaches a blind individual within a predefined distance, providing real-time auditory feedback about the identity of the approaching person. Through this groundbreaking approach, we're not only fostering independence but also promoting inclusivity, enabling visually impaired individuals to navigate social interactions with confidence and ease in a more accessible world.

 Requirements

- openCv
- pyttsx3
- ref_img.jpeg
- haarcascade_frontalface_default.xml

 Workflow of Face Distance Measurement

1. **Initialization:**
    - Import the necessary library, OpenCV (**`cv2`**).
    - Define the **`FaceDetector`** class.
    - Initialize class variables including **`known_distance`**, **`known_width`**, color definitions, font types, camera object, and face detector object.
    - Load the pre-trained face detection model (**`haarcascade_frontalface_default.xml`**).
2. **Focal Length Calculation:**
    - Define the **`focal_length`** method to calculate the focal length using the known distance, real width, and width of the object in the reference image.
3. **Distance Calculation:**
    - Define the **`distance_finder`** method to calculate the distance to the object using the focal length, real face width, and face width in the frame.
4. **Face Data Extraction:**
    - Define the **`face_data`** method to extract face-related data from the input image.
    - Convert the input image to grayscale.
    - Use the face detection classifier to detect faces in the image.
    - Iterate through the detected faces, calculate face width, and determine the center coordinates of each face.
    - If the **`distance_level`** is less than 10, set it to 10 (a condition for further processing).
5. **Main Execution:**
    - Define the **`run`** method to execute the main functionality of the face distance system.
    - Read a reference image (**`ref_image.jpeg`**) to calibrate the system.
    - Calculate the focal length using the reference image and known parameters.
    - Extract face-related data from the input frame.
    - Calculate the distance to the face in the frame using the focal length and known parameters.
    - Return the calculated distance
###  Object Detection and Gesture Recognition:
![archi](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/objectDetectionAndGesture-background.png)
#### 1.11 Gesture Recognition: 
 Introduction

Our project introduces a groundbreaking gesture recognition system designed to empower individuals with visual impairments by providing crucial information about their surroundings. This innovative system enables users to interact with their environment through hand gestures, offering real-time object detection feedback. For instance, when a visually impaired individual closes their hand, the system initiates object detection, providing auditory or tactile cues about nearby objects. Conversely, when the hand is opened, the system ceases object detection, ensuring privacy and minimizing distractions. By leveraging gesture recognition technology, our system aims to enhance the independence and safety of visually impaired individuals, enabling them to navigate and interact with their surroundings more confidently and efficiently.


 Requirements

- mediapipe
- numpy
- openCv

 Workflow of Gesture Recognition

1. **Initialization**:
    - Import necessary libraries and modules.
    - Define parameters and settings for the gesture recognition system.
    - Load pre-trained models for hand landmarks detection and classification.
    - Initialize object detection module.
2. **Run Method Invocation**:
    - The **`run()`** method is invoked with an image frame as input.
    - The current frames per second (FPS) are calculated.
    - The user can toggle between different modes and numbers using specific key inputs.
3. **Image Processing**:
    - Flip the input image horizontally to match the user's perspective.
    - Convert the image from BGR to RGB format for compatibility with the hand detection model.
    - Process the image using the MediaPipe Hands library to detect hand landmarks and handedness.
4. **Gesture Recognition**:
    - Extract hand landmarks and bounding rectangles for each detected hand.
    - Pre-process the landmark points for classification.
    - Classify hand gestures using a keypoint classifier and a point history classifier.
    - Update the gesture history based on the detected gestures.
    - If a closed hand gesture is detected, proceed to object detection. If an open hand gesture is detected, skip object detection.
5. **Object Detection**:
    - If a closed hand gesture is detected, initialize object detection to identify objects in the surrounding environment.
    - Perform object detection using the initialized module.
    - Provide feedback or relevant information to the user based on the detected objects.
6. **Visualization**:
    - Draw bounding rectangles around detected hands and landmarks on the image frame.
    - Display information such as handedness, hand sign, and finger gesture on the image.
    - Visualize the point history to track the movement trajectory of specific landmarks.
7. **User Interaction**:
    - Allow the user to toggle between different modes for logging hand gestures and point history.
    - Enable the user to specify a number for logging purposes.
8. **Logging**:
    - Log the normalized landmark points and finger gestures to CSV files based on the selected mode and number.
9. **Output**:
    - Return the hand sign ID as the output of the **`run()`** method.
    - Provide the debug image with visual annotations for display or further processing.

**Integration of TensorFlow Lite Model for Object Detection based on Hand Gestures**

This workflow incorporates object detection based on hand gestures, utilizing a TensorFlow Lite model for efficient inference on our device. Object detection is initiated only when a closed hand gesture is recognized, ensuring that system resources are utilized judiciously based on the user's gestures
#### 1.12 Object Detection:


 Introduction

We've harnessed the potential of object detection technology to revolutionize accessibility for the visually impaired community. By integrating state-of-the-art object detection algorithms into our system, we've created a seamless experience where users can effortlessly perceive their surroundings through auditory feedback. Object detection enables our system to identify and describe nearby objects in real-time, providing users with vital information about their environment. This innovative approach not only enhances independence but also promotes inclusivity by empowering visually impaired individuals to navigate the world with confidence and ease. Through cutting-edge technology and a commitment to accessibility, we're bridging the gap between sighted and non-sighted individuals, creating a more inclusive society for all.

 Requirements

- numpy
- threading
- openCv
- pyttsx3
- objectDetect_edgetpu.tflite
- labelmap.txt

 Workflow of Object Detection

---

**1. Initialization**:

- The `VideoStream` class is instantiated to capture live video frames from the camera.
- An instance of the `Detector` class is created to perform object detection on the captured frames using the MobileNetV2 model.

**2. Frame Capture and Processing**:
- The `VideoStream` class continuously grabs frames from the camera feed.
- Each captured frame is forwarded to the `Detector` class for object detection analysis.

**3. Gesture Recognition**:
- Before initiating object detection, the system checks for the presence of specific gestures, such as a closed hand gesture.
- If a closed hand gesture is recognized, object detection is initiated; otherwise, the system continues to capture frames without processing for object detection.

**4. Object Detection**:
- The `Detector` class utilizes a TensorFlow Lite model(edgeTPU), specifically MobileNetV2, to recognize objects within each frame.
- The model processes the frame, identifying objects and their corresponding confidence scores.
- Detected objects are marked with bounding boxes and labeled on the frame.

**5. User Feedback**:
- Using `pyttsx3`, a text-to-speech (TTS) module, the system converts the labels of detected objects into audible feedback for visually impaired users.
- To avoid redundancy, the system maintains a record of previously announced objects.

**6. Displaying Results**:
- The detected objects are visually highlighted on the frame by drawing bounding rectangles around them.
- The annotated frame, with bounding boxes and labels, is displayed in real-time to provide visual feedback to the user.

**7. Continuous Operation**:
- The system operates continuously, capturing, processing, and detecting objects in each incoming frame from the camera.

**8. Resource Management**:
- The system manages resources efficiently, ensuring the camera stream is properly released, and the system gracefully shuts down upon termination or interruption.

**9. Threading**:
- Threading is implemented to handle frame capture and object detection concurrently, enhancing system performance and responsiveness.
- This asynchronous execution prevents blocking of the main thread, enabling efficient frame processing.


  

### 1.13 Currency Recognition



 Introduction

We've developed a currency detection model tailored to assist visually impaired individuals in swiftly identifying Indian currency denominations. Using cutting-edge image recognition technology, our model offers real-time detection capabilities, instantly recognizing various currency notes. We have used  pyttsx3, a text-to-speech library, enabling the detected currency to be relayed audibly to users. This  not only enhances accessibility but also promotes independence and confidence in managing financial transactions for visually impaired individuals.

 Requirements

- tensorflow
- numpy
- openCv
- pyttsx3
- currency_edgetpu.tflite
- currency.txt

 Workflow of Currency Recognition

1. **Initialization**:
    - The **`ImageClassifier`** class is initialized with a voice assistant object, model path, and label path.
    - TensorFlow Lite Interpreter is initialized with the provided model path, and labels are loaded from the label path.
2. **Preprocessing**:
    - The **`preprocess_image`** method resizes the input image to match the model's input shape.
    - The resized image is normalized to the range [-1, 1] to prepare it for inference.
3. **Classification**:
    - The **`classify_image`** method processes the preprocessed image using the TensorFlow Lite model.
    - The output data containing classification results is obtained from the interpreter.
4. **Prediction**:
    - The **`predict`** method receives an image as input.
    - The image is classified using the **`classify_image`** method.
    - The predicted class and confidence score are extracted from the classification results.
    - If a new currency denomination is detected and not already in the **`currency`** list, it is added to the list.
    - The voice assistant speaks out the detected currency denomination to the user.
5. **Currency Detection and Output**:
    - If the detected currency denomination is new and not already in the **`currency`** list, it is added to the list.
    - The voice assistant announces the detected currency denomination to the user using pyttsx3 for text-to-speech output.
### 1.14 Optimizing Code using Threading

## Introduction

Our system employs multithreading to concurrently manage diverse modules. One thread oversees Gemini, Gemma, speech-to-speech, and OCR functionalities, ensuring seamless communication and text recognition. Another thread interfaces with PiApi to handle sensor data, including call, SMS, and location information, vital for navigation. A third thread employs depth estimation via Midas for precise distance calculation, aiding in obstacle avoidance. Finally, a fourth thread along with **Coral TPU (Tensor Processing unit)** orchestrates emotion detection, face recognition, gesture recognition, and object detection through Face Distance, enhancing user interaction and environmental awareness. This modular approach optimizes system performance, responsiveness, and functionality for visually impaired individuals.
![threading](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/thread-background.webp)
Workflow

1. **Initialization:**
    - Begin by initializing the system and all necessary modules.
2. **Thread 1: Gemini, Gemma, Speech-to-speech, OCR:**
    - Start the first thread to manage Gemini, Gemma, speech-to-speech conversion, and optical character recognition (OCR). These modules handle tasks related to text recognition, speech synthesis, and processing.
    
    <aside>
    💡 Gemini vision pro and Speech to speech is online with the help of **GSM Sim 7600 G H 4g LTE** due to its poor performance in offline but we also managed add offline backup using Whisper Tiny API for speech to speech and Gemma 2B 4qint for LLM capability
    
    </aside>
    
3. **Thread 2: PiApi for Sensor Interface:**
    - Launch the second thread dedicated to PiApi, which serves as the interface for all sensors and modules connected with Raspberry Pi 5.
    - Manage functionalities such as call handling, SMS processing, vibration alerts, location tracking, and utilizing the gyroscope module for fall detection.
4. **Thread 3: Distance Estimation with Midas:**
    - Initialize the third thread for distance estimation utilizing depth estimation through Midas.
    - This thread focuses on tasks related to estimating distances between objects and the visually impaired individual.
5. **Thread 4: Emotion Detection, Face Recognition, and Gesture/Object Recognition:**
    - Emotion detection systems swiftly categorize emotions like happiness, sadness, and anger, while face recognition capabilities ensure precise identification of individuals from digital images or video frames.
    - Our pioneering Face Distance technique measures facial feature distances to accurately infer emotions, enhancing our emotional detection capabilities significantly.
    - Gesture recognition interprets human gestures for applications like sign language translation, and object detection swiftly classifies objects within images or video streams.
    
    <aside>
    💡 Utilizing EdgeTpu Tflite models optimizes AI performance on Edge devices, ensuring smooth operation and responsiveness even in resource-constrained environments.
    
    </aside>
    
    - Seamless integration with Edge devices like Raspberry Pi with EdgeTpu and Google Coral devices, along with frameworks like TensorFlow Lite, simplifies deployment and management, maximizing AI potential in real-world applications.
6. **Integration and Interaction:**
    - Ensure seamless integration and interaction between threads to facilitate smooth communication and operation.
    - Enable each thread to share relevant data and insights as required for comprehensive system functionality.

Challenges

- Managing data sharing between Thread 3 and Thread 4 posed challenges, especially regarding access to Picamera2 data, necessitating a common data passing approach to ensure seamless integration of functionalities.
- Given resource constraints, optimizing code became imperative. Leveraging Tflite for most ML models significantly improved performance and outcomes, aligning with our goal of efficient resource utilization and enhanced results.
- Error handling to avoid Thread failure

## 2 Hardware
### Hardware Architecture:
![](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/Hardware-connection-background.png)
The hardware architecture consist of 

- Raspberry Pi 5
- Pi Camera 2 module
- Sim 7600X G-H Raspberry Pi hat module
- Coral USB Accelerator  TPU (Tensor Processing Unit)
- USB to Aux for headphone
- Gyroscope (Mpu6050)
- Vibration Motor
- 3D Model to house all the components



 Hardware Connectivity



The diagram illustrates the connectivity of various sensors and modules to the Raspberry Pi 5. Notably, the Coral TPU and earphones are connected to the Pi's USB port, while the SIM7600 for network connectivity utilizes both UART and USB for bidirectional communication. This setup ensures robust network connectivity and seamless data exchange.

The gyroscope employs the I2C interface for communication with the Raspberry Pi, offering precise motion sensing capabilities. Meanwhile, the camera is linked to the Pi via PCIe, facilitating high-speed data transfer and enabling advanced imaging functionalities.

Additionally, the vibration module interfaces with the Pi's GPIO pins, allowing for tactile feedback and enhancing user interaction. This comprehensive integration of diverse communication protocols and interfaces optimizes the Raspberry Pi 5's functionality across various domains.

 Challenges Faced

1. We attempted to utilize the M.2 Coral TPU A+E Key (https://coral.ai/products/m2-accelerator-ae) in conjunction with the Pineberry Hat AI (https://pineboards.io/products/hat-ai-for-raspberry-pi-5) as an interface between the TPU and Raspberry Pi. Despite investing over 100 hours in configuration and setup, the Coral TPU failed to register as connected. We made multiple adjustments to the Debian OS configuration file, but the TPU remained undetected in the PCIe channel.
During startup, an error concerning the MSI PCIe Address was also encountered. After exhaustive troubleshooting attempts, we concluded that the M.2 Coral TPU A+E Key might be faulty. Consequently, we reverted to using the USB Coral TPU, which was already in our possession and functioned seamlessly.



1. Setting up the TPU software for Raspberry Pi presented its own set of challenges, especially considering Google's discontinuation of support since 2019. The PyCoral library, a critical component, was compatible only with Python version 3.9. However, the Picamera2 Python library, essential for camera operations, required Python version 3.11. This compatibility conflict made it impossible to run both libraries simultaneously.
**Solution**: After extensive research and a night of troubleshooting, we discovered multiple open-source contributions that addressed this issue. These contributions enabled the PyCoral library to function seamlessly on Python version 3.11 and also provided an updated TensorFlow Lite runtime that supported the specific PyCoral version. This breakthrough not only resolved the compatibility hurdles but also ensured smooth integration and operation of the TPU software on the Raspberry Pi.
2. Initially, obtaining internet connectivity posed a challenge when using the GSM Module. We opted for the Sim 808 Module, which not only facilitated calling, receiving messages, and establishing network connectivity but also offered GPS functionality. However, we encountered limitations with only 2G network access, resulting in sluggish responses from the Gemini API and speech recognition processes.
    
    **SIM 808 Module**
    
    
    **Solution:** To address this, we switched to the Sim7600X G-H Raspberry Pi Hat. This alternative not only integrated GPS capabilities but also provided 4G LTE internet connectivity for the Raspberry Pi 5. This upgrade significantly enhanced our system's responsiveness to cloud models, ensuring smoother and faster operations.
    
### 2.1 SIM7600 G-H Module

 **Overview**

- The SIM7600G Raspberry Pi HAT is a versatile add-on board that facilitates cellular communication for the Raspberry Pi 5. It integrates the SIM7600G module, providing capabilities for making calls, sending messages, and accessing cellular data 4 G LTE Network
![archi](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/sim7600g.png)
<aside>
💡 This provide 4g LTE Network which allow us to run Speech - Text and Gemini LLM Online with faster Response which improves user experience

</aside>

 **Hardware Setup**

- **Physical Connection**: Carefully attach the SIM7600G HAT to the Raspberry Pi 5 GPIO header, ensuring proper alignment.
- **Power Supply**: Use a stable power supply capable of providing sufficient current to both the Raspberry Pi and the SIM7600G module. Voltage requirements and current consumption should be considered to prevent power-related issues.
- **SIM Card Installation**: Insert a compatible SIM card into the SIM card slot on the module, ensuring it is properly seated.

 **Software Setup**

- **Driver Installation**: Install the necessary drivers and software libraries for the SIM7600G module on the Raspberry Pi 5.
- **Serial Communication Configuration**: Configure the Raspberry Pi to communicate with the SIM7600G module via serial communication. Set up serial port settings, such as baud rate and data bits, to match the module's specifications.
- **Python Library Installation**: Install the Python library provided by the manufacturer to interface with the SIM7600G module. This library simplifies communication with the module and provides high-level functions for call, message, and data operations.

Features

 **Making Calls:**

- **Functionality**: Utilize the provided Python library to initiate outgoing calls from the Raspberry Pi.
- **Usage**: Call the designated phone number by invoking the appropriate function from the library, passing the phone number as an argument.
- **Error Handling**: Implement error handling mechanisms to manage potential issues, such as network unavailability or call failure.

 **Sending Messages:**

- **Functionality**: Send SMS messages from the Raspberry Pi using the SIM7600G module.
- **Usage**: Invoke the messaging function from the Python library, providing the recipient's phone number and the message content as parameters.
- **Confirmation**: Confirm successful message transmission and handle any errors encountered during the process.

 **Cellular Data Connection:**

- **Establishment**: Set up a cellular data connection to enable internet access on the Raspberry Pi.
- **Configuration**: Configure the Access Point Name (APN) settings for the cellular network provider.

 Challenges

- **Power Management**: Addressing power supply challenges to ensure stable operation of both the Raspberry Pi and the SIM7600G module.
- Configuring PI 5 for PPP Protocol (point to point protocol) to establish 4G LTE internet connection with pi
    
### 2.2 Fall Detection 
![](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/alert-background.png)
The MPU-6050 IMU (Inertial Measurement Unit) is a sensor that combines a 3-axis accelerometer and a 3-axis gyroscope. The accelerometer measures gravitational acceleration, while the gyroscope measures rotational velocity. Additionally, this module includes a temperature sensor. It's commonly used for determining the orientation of a moving object.

MPU6050 Pinout:

| Pin | Function |
| --- | --- |
| VCC | Power the sensor (3.3V or 5V) |
| GND | Ground (Common) |
| SCL | I2C Clock (A5) |
| SDA | I2C Data (A4) |
| XDA | I2C Data for additional sensors |
| XCL | I2C Clock for additional sensors |
| AD0 | I2C Address Selection |
| INT | Interrupt (Indicates new data) |
| POWER | Power Consumption (3.6mA) |

Connections:

1. Enable I2C on the Raspberry Pi:
    - Run `sudo raspi-config` in the terminal.
    - Select `Interfacing Options > I2C`.
    - Enable the I2C interface and kernel module loading.
    - Reboot when prompted.
2. Connect the MPU6050 to the Raspberry Pi:
    - VCC to 3.3V pin.
    - GND to Ground.
    - SDA to SDA pin.
    - SCL to SCL pin.
3. Install the MPU6050 library:
    - Run `sudo apt install python3-smbus` in the terminal.
    - Run `pip install mpu6050-raspberrypi`.

Code Explanation:

The code sets up serial communication at 9600 baud rate. In the loop function, it reads raw data from the sensor using `mpu_read()`. The raw data is then converted into meaningful values such as acceleration and angular velocity in x, y, and z directions. It calculates the amplitude vector for 3-axis acceleration and checks if it falls below a certain threshold, setting `trigger1` to true if so. If `trigger1` is true, it increments `trigger1count` and checks if the amplitude vector exceeds another threshold, setting `trigger2` to true if so. If `trigger2` is true, it increments `trigger2count` and calculates angular change in x, y, and z directions. If the change is between 80-100 degrees, `trigger3` is set to true. If `trigger3` is true, it increments `trigger3count` and checks if it exceeds a threshold, setting `fall` to true and printing "FALL DETECTED". If `fall` is true, it resets and prints "FALL DETECTED". The code also checks if `trigger1count`, `trigger2count`, and `trigger3count` exceed thresholds and sets corresponding variables to false.

MPU6050 Features:

- MEMS 3-axis accelerometer and 3-axis gyroscope
- Power Supply: 3-5V
- Communication: I2C protocol
- Built-in 16-bit ADC for accuracy
- Built-in DMP for computational power
- Can interface with other IIC devices
- Configurable IIC Address
- Built-in temperature sensor

Alternatives:

- ADXL335 (3-axis accelerometer)
- ADXL345 (3-axis accelerometer)
- MPU9250 (9-axis IMU)

Results:

Using a gyroscope sensor for fall detection shows promising outcomes in accuracy improvement and reduction of false positives and negatives in fall detection systems. By combining accelerometers and gyroscopes, algorithms have been developed to enhance accuracy while minimizing errors.


### 2.3 **Vibration Motor: Enhancing Safety Measures**

In the realm of safety measures, the vibration motor emerges as a crucial component to alert users promptly in various scenarios, such as detecting obstacles or receiving notifications from caregivers.

 **Introduction**

Vibration motors are compact devices designed to generate vibrations when powered, making them ideal for alert systems. These motors are particularly useful in situations where audible alarms might not be practical or when users need discreet notifications.
**Key Features:**

- **Operating Voltage (VDC):** 3 ~ 5.3
- **Motor Diameter:** 10mm
- **Rated Speed:** 9000 RPM (min)
- **Rated Voltage (V):** 5
- **Rated Current:** up to 60 mA
- **Starting Current:** up to 90 mA
- **Starting Voltage:** 3.7 VDC
- **Insulation Resistance:** 10 MΩ
- **Dimensions (mm):**
    - Length: 23.5
    - Width: 21
    - Height: 8
- **Weight (g):** 3

 **Application and Usage**

**Alert Systems:**

Vibration motors are commonly used in alert systems to notify users of important events or potential hazards. For instance, in wearable devices or assistive technologies, these motors provide discreet feedback to users without disturbing their surroundings.

 **Safety Measures:**

In safety-critical applications, such as navigation aids for the visually impaired or industrial safety equipment, vibration motors play a vital role in alerting users to obstacles or unsafe conditions.

 **Caregiver Notifications:**

Caregivers can use vibration motors as part of monitoring systems to alert them when their attention is needed. This ensures timely responses to the needs of the person under their care.

**Connecting the Vibration Motor**

Connecting the vibration motor to a Raspberry Pi or Arduino is relatively straightforward. Typically, you'll connect the GND (ground) pin to the ground, the VCC (power) pin to a power source (5V), and the VIN pin to a digital pin for control.


 **Conclusion**

In conclusion, vibration motors are invaluable tools for enhancing safety and providing timely notifications in various applications. Whether it's alerting users to obstacles, ensuring their safety, or facilitating caregiver communication, these compact devices offer versatile solutions with minimal intrusion and maximal effectiveness.

### 2.4 TPU (Tensor Processing Unit)

We employ TPU (Tensor Processing Unit) technology to enhance the local execution performance of ML (Machine Learning) Lite models. This implementation not only optimizes the execution speed but also alleviates the computational load on the CPU. This strategic offloading of tasks to the TPU enables us to concurrently run resource-intensive models such as text-to-speech and speech-to-text transformations on the CPU while efficiently managing continuous tasks like object detection on the TPU. This segregation of tasks ensures that each component operates at its peak efficiency, contributing to overall system performance and responsiveness.


 Requirement
- Coral TPU
- Pycoral
- Tflite-run-time
- Python ≥3.9.16
- pyenv
- picamera2
- cv2

Setting UP

Setting up my TPU was quite the challenge. It required Python 3.9, but my PiCamera2 needed 3.11, leading me to manage multiple Python versions with pyenv. I faced a dilemma: either downgrade the camera or explore alternatives like pycoral version 3.11 or the TFLite runtime.

Opting for the latter, I first attempted the TFLite runtime, realizing it needed the edge variant. After running edgetup.tflite, my TPU finally started functioning. However, I still desired the functionality of the pycoral library, despite Google discontinuing support in 2019. Integrating it was tricky due to version mismatches, but I stumbled upon a solution by [feranick](https://github.com/feranick/pycoral/releases/tag/v2.0.1TF2.16.1), who had compiled a version compatible with Python 3.11.

After downloading and implementing feranick's version of pycoral, I successfully completed the TPU setup. It was a journey of perseverance, but the end result was worth it.



 Workflow

We developed our object detection and gesture recognition models as EdgeTPU TFLite models, specifically using uint8 quantization. These models are utilized for object detection; when the system detects a "wrist close" gesture, it activates the object detection function to identify objects. Conversely, when the user opens their wrist, the system stops detecting objects, optimizing resource utilization and response time.
*Benchmarks**

### 2.5 Pyapi:
 Introduction

The PI API serves as the pivotal interface connecting a myriad of sensors and modules seamlessly integrated with the Raspberry Pi 5. These modules encompass critical functionalities tailored to enhance the daily experiences of visually impaired individuals. From facilitating essential communication through call and SMS features to providing real-time alerts via vibration, the PI API ensures swift access to assistance. Moreover, with capabilities like object proximity detection and navigation assistance, it empowers users to navigate their surroundings with confidence. Furthermore, leveraging gyroscope technology, the API swiftly alerts caregivers in the unfortunate event of a fall, prioritizing user safety and well-being. This comprehensive suite of functionalities underscores our commitment to fostering independence and enhancing the quality of life for visually impaired individuals.

 Requirements

- pynmea2
- python-gsmmodem-new
- mpu6050-raspberrypi
- gpiod
- **serial**
- Google Speech Recognition
- pyttsx3

 Workflow of pyAPI

1. **Initialization:** The **`piAPI`** class is initialized with necessary dependencies such as the voice assistant and database connection. Various modules including GPS, GSM, gyro, and vibration are set up during initialization.
2. **GPS Setup:** The **`setUpGPS()`** method initializes GPS functionality by establishing a serial connection and activating GPS sessions. Location data is retrieved periodically using the **`getLocation()`** method, which parses NMEA messages to obtain latitude and longitude coordinates.
3. **GSM Setup:** The **`setupGSM()`** method initializes GSM functionality, allowing the device to make phone calls and send SMS messages. Incoming calls are handled by the **`handleIncomingCall()`** method, which alerts the user and automatically answers after multiple rings.
4. **Phone Call:** The **`callPhone()`** method initiates a phone call to a specified number. The GPS session is stopped before making the call, and resumed after the call ends.
5. **SMS Sending:** The **`sendSms()`** method sends an SMS message to a specified number. Similar to phone calls, the GPS session is temporarily stopped during SMS transmission.
6. **Gyro Setup:** The **`setupGyro()`** method initializes the gyroscope module, which is used to detect falls. Acceleration data is obtained from the MPU6050 sensor, and fall detection is performed based on predefined threshold values.
7. **Fall Detection:** The **`listenGyro()`** method continuously monitors acceleration data from the gyroscope. If the magnitude of acceleration falls below a predefined threshold, indicating a potential fall, the **`fallDetected`** flag is set.
8. **Vibration Setup:** The **`setupVibrate()`** method initializes the vibration functionality, allowing the device to provide tactile feedback. Vibration is controlled using GPIO pins, with the **`vibrateMotor()`** method toggling the vibration motor on and off for a specified duration.
9. **Fall Alert:** If a fall is detected, the device triggers the vibration motor to alert the user. This alert mechanism aims to notify caregivers or nearby individuals in case of emergencies.

## 3 Software

### 3.1 Realtime Tracking:
![caregiver app](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/caregiver%20app.png)

Feature

In our mobile app, caregivers can monitor the location of Sixth Sense users in real-time using the GPS module in the Sim7600 device. We utilize Firebase to ensure seamless real-time tracking. Additionally, we've integrated the Direction API for convenient navigation to Sixth Sense users.

Tech Stack

- React Native
- React native google map
- firebase
- Google maps API
- direction API
- Native-Alert

Working

1. **GPS Module (Sim7600):**
    - The Sim7600 module is a GPS/GNSS module that provides accurate location data.
    - It communicates with satellites to determine the device's current coordinates (latitude and longitude).
    - This data is then sent to the mobile app for processing and display.
2. **Firebase Realtime Database:**
    - Firebase is used as a backend service to store and sync location data in real-time.
    - When the GPS module sends new location updates, these updates are immediately sent to Firebase.
    - Caregivers and authorized users can access this data through the mobile app, ensuring they have up-to-date information on the Sixth Sense user's location.
3. **Direction API Integration:**
    - The Direction API is integrated into the app to provide navigation assistance.
    - When a caregiver wants to reach the Sixth Sense user, they can input their location and the destination (Sixth Sense user's location) into the app.
    - The Direction API calculates the best route, considering factors like traffic conditions and distance, and provides turn-by-turn navigation instructions to the caregiver.
4. **Real-Time Monitoring Process:**
    - The caregiver opens the mobile app and accesses the Sixth Sense monitoring feature.
    - The app continuously fetches the latest location data from Firebase, showing the real-time location of the Sixth Sense user on a map.
    - If the caregiver needs to navigate to the user, they can initiate the navigation feature within the app, which utilizes the Direction API for route guidance.

Overall, this system ensures that caregivers can monitor the Sixth Sense user's location in real-time, enabling them to provide timely assistance and support as needed.
### 3.2 Geofencing
![geofencing](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/Frame%20129.png)
Domain
Mobile App - React Native
Feature
In the mobile app the caregiver now have the ability to monitor the blind by setting a circle of radius x position in a map, whenever the the sixth-sense user (blind) leave or move out of the circle the caregiver will receive a alert notification saying the user has left the safezone. this feature allows the caregiver to be alert and proactive even if they are not using the mobile phone thus can improve safety of the blind by taking immediate active and setup.
 Tech Stack

- React Native
- React native google map
- expo-task-manager
- expo-backgroundfetch
- firebase

 Working

In geofence page, User have the ability to select location of the circle fence on the map by clicking where they want to, after choosing a position the user will have radius slider this give user ability to increase and decrease the radius of the circle after hitting save this will get stored in firebase. the main logic is comparing the distance from the center of the circle and the sixth sense user location (blind) with the radius of the circle. if the distance is more than the radius then the blind is out of the safe zone else the user is inside the safe zone. the distance is calculated using haversine formula 

 Formula

haversineFormula(center of circle, sixth sense user location) > radius of the circle

### 3.3 Messaging 
![message](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/Frame%20178.png)
Domain
React native - Mobile App
**Messaging Feature Overview**

1. **Previous Functionality**: Initially, blind users could send messages using voice commands like "Send Message," which would be sent to the caregiver app.
2. **Updated Messaging Tab**: Now, there's a dedicated messaging tab within the app where caregivers can type and send messages directly to blind users.
3. **Text-to-Speech Conversion**: Messages received by blind users are read aloud using machine learning models that convert text to speech specifically tailored for them.
   
**Tech Stack**

- **React Native**: Used for developing the mobile app, ensuring cross-platform compatibility.
- **Firebase**: Utilized for real-time data storage and synchronization, specifically for storing messages sent between caregivers and blind users.
- **File**: Likely used for storing additional data or configurations related to the messaging feature.
**Working Process**

1. **Caregiver Message Input**: Caregivers have an input field where they can type messages.
2. **Message Sending**: Once a caregiver sends a message, it is sent to Firebase for storage and synchronization.
3. **Message Reception by Blind Users**: The Program running on the blind user's device continuously checks the message collection in Firebase for any new messages from caregivers.
4. **Inbox Handling**: When a new message is received, it's stored in a data structure resembling a Last-In-First-Out (LIFO) queue or stack, essentially creating an inbox for the blind user.
5. **Message Reading**: When the blind user requests to read messages, the app reads the messages from the inbox in LIFO order, ensuring they hear the most recent message first.

This setup provides an efficient way for caregivers to communicate with blind users using text messages, with the app handling message storage, retrieval, and text-to-speech conversion seamlessly.

### 3.4 People
 Feature

Place where caregiver can upload people faces with name. its is used in ml part to recognize who is front of them with emotion

 Tech Stack

- React Native
- Firebase

 Working

1. **Face Upload Feature:**
    - In the mobile app, caregivers have a dedicated section where they can upload photos of individuals along with their corresponding names.
    - Caregivers capture or upload images directly from their device's camera or gallery.
    - They input the person's name or any relevant information associated with them.
2. **ML Model for Facial Recognition and Emotion Detection:**
    - The app integrates a trained ML model for facial recognition and emotion detection.
    - This model is capable of recognizing faces in images and analyzing facial expressions to determine emotions such as happiness, sadness, anger, etc.
3. **Integration of Face Database:**
    - The uploaded images and corresponding names are stored in a face database within the app's backend system.
    - This database acts as a reference for the ML model during the recognition process.
4. **Facial Recognition and Emotion Detection Process:**
    - When the app's camera is activated or an image is uploaded, the ML model is invoked to analyze the faces present in the image.
    - The model compares the detected faces with the images stored in the face database to identify individuals.
    - Simultaneously, it analyzes facial expressions to determine the emotional state of the person(s) in the image.
5. **Output and User Interaction:**
    - The app displays the recognized person's name along with their detected emotions on the user interface.
    - Caregivers can view this information in real-time, helping them understand the emotional state of the individual they are interacting with.
### 3.5 Multi Language Support 

---

 Domain

React Native - Mobile App

**Objective:**

Enable caregivers to change the language of the mobile app between Hindi and English, with provisions for adding more languages in the future.

**Tech Stack:**

- React Native
- i18n-js
- i18next
- react-i18next

**Implementation:**

1. **Install Dependencies:** Begin by installing the necessary packages using npm or yarn.
2. **Setup i18n Configuration:** Create an **`i18n.js`** file to configure i18n, define available languages (e.g., English and Hindi), and set up default and fallback languages.
3. **Create Language JSON Files:** In a **`locales`** folder, create JSON files for each supported language (e.g., **`en.json`** for English and **`hi.json`** for Hindi) containing key-value pairs for translated strings.
4. **Implement Language Switching:** In React Native components, use the **`useTranslation`** hook from **`react-i18next`** to access translations. Implement language switch buttons or dropdowns that call **`i18n.changeLanguage`** to switch between languages.
5. **Testing and Deployment:** Test the language switching functionality thoroughly to ensure translations are displayed correctly based on the selected language. Deploy the app with multi-language support enabled.

**Conclusion:**

By following these steps, caregivers can seamlessly change the language of the React Native mobile app, providing a localized experience for users in Hindi and English, with extensibility to support additional languages in the future.


### 3.6 Contact 

**Domain:**

Raspberry Pi 5 - Hardware and React Native - Mobile App

**Feature:**

This feature enables blind users (sixth sense users) to make calls to contacts stored in a database through a caregiver app using voice commands. The mic detects the command **“Call <Name of the user stored in caregiver app>”**, converts speech to text, and initiates the call via a GSM module, all managed on the sixth sense hardware. The mobile app provides an interface for adding contacts due to the blind user's difficulty in manual entry.

**Tech Stack:**

- React Native
- Firebase
- SIM 808 Module

**Future Scope:**

- [ ]  Implementing contact saving functionality on the sixth sense hardware.
- [ ]  Adding voice commands for blind users to save contacts.

**Working:**

1. **Command Initiation:**
    - The blind user initiates the call cycle by voicing the command, e.g., **“Call Hursun”**.
    - A machine learning (ML) model translates the voice command to text.
2. **Database Lookup:**
    - The text data is cross-checked against the database to verify if the contact name exists.
    - If found, the corresponding phone number is retrieved.
3. **Call Initiation:**
    - The retrieved phone number is used to initiate a call via the GSM SIM 808 module on the sixth sense hardware.
    - Multiple functions like call initiation, hang up, and other call-related actions are supported.

**Enhancements:**

The feature facilitates seamless communication for blind users by leveraging voice commands and advanced hardware capabilities. Future enhancements aim to add more functionalities and improve user interaction, such as adding voice commands for contact saving directly on the sixth sense hardware.
### 3.7 Step by Step Navigation:

  Introduction

In our system, we seamlessly integrate step-by-step navigation to aid visually challenged individuals in navigating their surroundings. Leveraging requests, geopy, and the Google Maps API, we calculate distances between coordinates, customizing guidance. Through the Google Distance API, we offer personalized route planning based on the user's input obtained via Google Speech Recognition. Additionally, we utilize text-to-speech functionality with pyttsx3, enabling users to receive step-by-step instructions audibly. This comprehensive approach enhances independence, empowering users to confidently navigate to their destinations while considering factors like accessibility and safety. By providing reliable navigation assistance, our system improves mobility and access to essential services, ultimately enhancing the overall quality of life for visually challenged individuals.
![back](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Flowchart%20Images/navigation-background.png)
 Requirements

- geopy
- Google Speech Recognition
- pyttsx3
- requests

 Workflow of Navigation

1. **Initialization**:
    - The **`NavigateUser`** class is initialized with the necessary parameters, including a **`voice_assistant`** object and the user's coordinates.
2. **Command Initiation**:
    - Upon receiving the command "Sense navigate," the system triggers the navigation process by calling the **`setupNavigation`** method.
3. **Setup Navigation**:
    - When the user requests navigation by providing an address, the **`setupNavigation`** method is called.
    - The provided address is converted into geographical coordinates using the Mapbox Geocoding API.
    - Then, the user's current coordinates and the destination coordinates are used to fetch navigation directions from the Mapbox Directions API.
    - If successful, the navigation steps are extracted, and the voice assistant speaks the first instruction.
4. **Navigation Process**:
    - The **`navigate`** method is called iteratively within a loop while the user is navigating.
    - It checks if step-by-step navigation is active and if there are remaining steps to follow.
    - For each step, it calculates the distance between the user's current position and the next maneuver location.
    - If the user is within 20 meters of the next maneuver, the current step is completed, and the voice assistant speaks the next instruction.
    - Once all steps are completed, the voice assistant announces that the destination is reached, and navigation stops.
5. **Stop Navigation**:
    - If the user decides to stop navigation, the **`stopNavigation`** method is called, and the navigation process is terminated.


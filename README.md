<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Sixth Sense](#sixth-sense)
    - [Architecture:](#architecture)
    - [Technology Arsenal:](#technology-arsenal)
  - [1 .Machine Learning:](#1-machine-learning)
    - [1.1. Optical Character Recognition(OCR)](#11-optical-character-recognitionocr)
    - [1.2. Natural Language Processing(NLP) using Spacy](#12-natural-language-processingnlp-using-spacy)
    - [1.3. Optimisation of Code](#13-optimisation-of-code)
    - [1.4. Gemini](#14-gemini)
    - [1.5. Multiprocessing using ProcessPoolExecutor](#15-multiprocessing-using-processpoolexecutor)
    - [1.6. Voice Assistant](#16-voice-assistant)
    - [1.7. Google Calendar API](#17-google-calendar-api)
    - [1.8. Distance Warning system using Midas 2.1V small](#18-distance-warning-system-using-midas-21v-small)
  - [2 Software](#2-software)
    - [2.1 Geofencing](#21-geofencing)
    - [2.2 Messaging](#22-messaging)
    - [2.3 Multi Language Support](#23-multi-language-support)
    - [Contact](#contact)
  - [3 Hardware](#3-hardware)
    - [3.1 Fall Detection](#31-fall-detection)
    - [3.2 **Vibration Motor: Enhancing Safety Measures**](#32-vibration-motor-enhancing-safety-measures)
    - [3.3 TPU (Tensor Processing Unit)](#33-tpu-tensor-processing-unit)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->




# Sixth Sense

<div style="text-align: center;">
    <img src="https://github.com/Kishorecoder96/sixth-_sense/blob/main/logo.png" alt="logo" style="width: 100px; height: 100px;">
</div>

![sixth sense](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/sixth%20sense.png)
#### Generations:
![geberation](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/Logo.png)


### Architecture:
# Architecture

The hardware architecture consist of 

- Raspberry Pi 5
- Pi Camera 2 module
- Sim 7600X G-H Raspberry Pi hat module
- Coral USB Accelerator  TPU (Tensor Processing Unit)
- USB to Aux for headphone
- Gyroscope (Mpu6050)
- Vibration Motor
- 3D Model to house all the components





## Hardware Connectivity
The diagram illustrates the connectivity of various sensors and modules to the Raspberry Pi 5. Notably, the Coral TPU and earphones are connected to the Pi's USB port, while the SIM7600 for network connectivity utilizes both UART and USB for bidirectional communication. This setup ensures robust network connectivity and seamless data exchange.

The gyroscope employs the I2C interface for communication with the Raspberry Pi, offering precise motion sensing capabilities. Meanwhile, the camera is linked to the Pi via PCIe, facilitating high-speed data transfer and enabling advanced imaging functionalities.

Additionally, the vibration module interfaces with the Pi's GPIO pins, allowing for tactile feedback and enhancing user interaction. This comprehensive integration of diverse communication protocols and interfaces optimizes the Raspberry Pi 5's functionality across various domains.

## Challenges Faced

1. We attempted to utilize the M.2 Coral TPU A+E Key (https://coral.ai/products/m2-accelerator-ae) in conjunction with the Pineberry Hat AI (https://pineboards.io/products/hat-ai-for-raspberry-pi-5) as an interface between the TPU and Raspberry Pi. Despite investing over 100 hours in configuration and setup, the Coral TPU failed to register as connected. We made multiple adjustments to the Debian OS configuration file, but the TPU remained undetected in the PCIe channel.
During startup, an error concerning the MSI PCIe Address was also encountered. After exhaustive troubleshooting attempts, we concluded that the M.2 Coral TPU A+E Key might be faulty. Consequently, we reverted to using the USB Coral TPU, which was already in our possession and functioned seamlessly.

1. Setting up the TPU software for Raspberry Pi presented its own set of challenges, especially considering Google's discontinuation of support since 2019. The PyCoral library, a critical component, was compatible only with Python version 3.9. However, the Picamera2 Python library, essential for camera operations, required Python version 3.11. This compatibility conflict made it impossible to run both libraries simultaneously.
**Solution**: After extensive research and a night of troubleshooting, we discovered multiple open-source contributions that addressed this issue. These contributions enabled the PyCoral library to function seamlessly on Python version 3.11 and also provided an updated TensorFlow Lite runtime that supported the specific PyCoral version. This breakthrough not only resolved the compatibility hurdles but also ensured smooth integration and operation of the TPU software on the Raspberry Pi.
2. Initially, obtaining internet connectivity posed a challenge when using the GSM Module. We opted for the Sim 808 Module, which not only facilitated calling, receiving messages, and establishing network connectivity but also offered GPS functionality. However, we encountered limitations with only 2G network access, resulting in sluggish responses from the Gemini API and speech recognition processes.
    
    **SIM 808 Module**
    
    **Solution:** To address this, we switched to the Sim7600X G-H Raspberry Pi Hat. This alternative not only integrated GPS capabilities but also provided 4G LTE internet connectivity for the Raspberry Pi 5. This upgrade significantly enhanced our system's responsiveness to cloud models, ensuring smoother and faster operations.
    
    
#### Old Architecture
![Old Archictecture](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/Old%20architecture%20(2).png)
#### New Architecture
![New Architecture](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/New%20architecture.png)
### Technology Arsenal:
1. Firebase <img width="30" height="20" src="https://img.icons8.com/color/48/firebase.png" alt="firebase"/> - Infrastructure and Security: Provides a reliable and scalable backend with built-in security features for data management and user authentication.
2. React Native <img width="30" height="20" src="https://img.icons8.com/officel/30/react.png" alt="react"/> - App for Caretaker: Cross-platform mobile application framework ensuring a consistent user experience across different devices and operating systems.
3. Pi OS <img width="30" height="20" src="https://img.icons8.com/color/48/raspberry.png" alt="raspberry"/>- Lightweight and Automation: Optimized operating system for Raspberry Pi devices, conserving resources and enabling automation tasks.
4. Gemini  - Personal Companion: Core intelligence system offering environmental awareness, navigation, alerts, and voice messaging for personalized assistance.
5. OpenCV <img width="30" height="20" src="https://img.icons8.com/color/48/opencv.png" alt="opencv"/>- Face Recognition: Utilized for facial recognition functionalities to enhance security and provide personalized assistance.
6. Torch - Speech to Text: Enables voice command interaction through speech-to-text conversion, enhancing accessibility and user experience.
7. OCR <img width="30" height="20" src="https://img.icons8.com/material/24/printed-ocr.png" alt="printed-ocr"/>- Extracting Images: Extracts text from images to improve comprehension and facilitate data processing.
8. Google Maps API <img width="30" height="20" src="https://img.icons8.com/color/48/google-maps-new.png" alt="google-maps-new"/>- Directions API: Integrates reliable navigation information from Google Maps for safe and efficient travel planning.
9. Google Calendar API <img width="30" height="20" src="https://img.icons8.com/color/48/google-calendar--v2.png" alt="google-calendar--v2"/>:provide virtual assistant functionalities, including accessing calendar events and creating notes using speech recognition and text-to-speech.
10. Coral TPU <img width="30" height="20" src="https://img.icons8.com/office/30/coral.png" alt="coral"/>- Accelerated Machine Learning: Integrates Coral TPU for accelerated machine learning tasks, enhancing performance and efficiency.
11. TensorFlow Lite - Lightweight Machine Learning: Utilizes TensorFlow Lite for deploying machine learning models on resource-constrained devices, optimizing performance on edge devices.
12. MediaPipe - MediaPipe is chosen for its real-time hand tracking and gesture recognition capabilities, allowing the device to understand hand movements and translate them into action
13. Google Speech-To-Text <img width="30" height="20" src="https://img.icons8.com/ios-glyphs/30/speech-to-text.png" alt="speech-to-text"/>-  converts speech to text for situations where an internet connection allows real-time processing for greater accuracy and features. 
14. Whisper Speech-To-Text <img width="30" height="20" src="https://img.icons8.com/ios-filled/50/whisper.png" alt="whisper"/> - For offline use, our device employs a built-in speech recognition model for real-time speech-to-text conversion, ensuring functionality without an internet connection
15. pyttsx3 - converts text to speech on your device itself (locally), providing voice feedback without needing an internet connection. 
16. langchain -  acts as a bridge, smoothing communication between the user and Gemini. It refines the questions and requests for optimal understanding by the large language model.
17. Face-Recognition <img width="30" height="20" src="https://img.icons8.com/external-flat-circular-vectorslab/68/external-Face-Recognition-interior-flat-circular-vectorslab.png" alt="external-Face-Recognition-interior-flat-circular-vectorslab"/>- it recognizes faces, helping identify people visually imapired individual meet.
18. pyaudio - it acts as a microphone, capturing spoken words for the device to understand.
19. geopy - it bridges the gap, calculating distances between locations based on their coordinates.
20. easyocr - it empowers the device to "read" text, converting images of characters to digital text.

## 1 .Machine Learning:
### 1.1. Optical Character Recognition(OCR)

**Introduction:**
The OCR module is specifically designed to assist visually impaired individuals in accessing textual content from images. Leveraging the EasyOCR library, it provides a user-friendly interface for extracting text from various sources, thereby enhancing accessibility and independence for individuals with visual impairments. 

**Implementation:**
The OCR module utilizes the EasyOCR library to process images and extract text. It offers a simplified interface for text extraction, requiring minimal user interaction. By leveraging OpenCV for image processing, the module ensures efficient and accurate recognition of textual content from diverse sources, including printed materials, digital documents, and handwritten notes.

**Benefits for Visually Impaired Individuals:**

1. **Accessible Information:** The OCR module enables visually impaired individuals to access textual information from a wide range of sources, including books, documents, labels, and signs, which may otherwise be inaccessible to them.
2. **Independence:** By providing the ability to extract text independently, the module empowers visually impaired users to access information without relying on sighted assistance, promoting self-reliance and confidence.
3. **Real-Time Feedback:** With its quick and efficient text extraction capabilities, the module offers real-time feedback, allowing users to instantly access and interact with textual content in their environment.
4. **Multilingual Support:** Supporting multiple languages, the module caters to the diverse linguistic needs of visually impaired individuals, facilitating access to information in their preferred language.

**Integration with Sixth Sense:**
The OCR module has been integrated with Sixth Sense to enhance its usability and accessibility for visually impaired users. By leveraging our existing assistive technologies, the module extends its functionality and ensures compatibility with diverse user preferences and needs.

**Voice Command Integration:**
The OCR module features voice command integration, allowing visually impaired users to interact with the system using voice commands. Users can issue commands such as "take a picture" to capture an image using the device's camera. Additionally, they can say "extract text from the image" to initiate text extraction using the OCR module.



###  1.2. Natural Language Processing(NLP) using Spacy

**Overview**

This code implements a voice-controlled assistant system that utilizes natural language processing (NLP) to interpret user commands and perform various tasks. The system integrates functionalities such as image processing, text extraction, notification sending, message sending, and currency detection. The primary goal of using NLP in this context is to enable intuitive interaction with the assistant by understanding and responding to spoken commands.

**Usage of Natural Language Processing (NLP)**

1. **Command Interpretation**:
    - **Purpose**: NLP is employed to interpret user commands provided through voice input.
    - **Implementation**: The **`spacy`** library is used to process and analyze the input text, allowing the system to identify key elements such as verbs, nouns, and adjectives.
    - **Example**: Commands like "take a photo," "send a message," "detect currency," and "alert" are identified and processed using NLP techniques.
2. **Task Execution Based on Commands**:
    - **Purpose**: After interpreting user commands, the system executes corresponding tasks based on the identified actions.
    - **Implementation**: Conditional statements are used to check for specific keywords or phrases indicative of different actions, such as capturing a photo, sending a message, or detecting currency. NLP is leveraged to identify these keywords and trigger the appropriate functions accordingly.
    - **Example**: If the user mentions "alert," the system sends a notification with an emergency message. Similarly, commands related to sending messages or capturing photos are executed based on NLP-based command interpretation.

**Conclusion**

The integration of natural language processing enables intuitive interaction with the voice-controlled assistant system. By interpreting user commands and executing tasks based on the identified actions, the system provides a seamless user experience. Ongoing enhancements and refinements to the NLP model can further improve the accuracy and effectiveness of command interpretation, enhancing the overall usability of the system.
 
 
### 1.3. Optimisation of Code

 Overview

This document outlines the refactoring process for the SixthSense project, focusing on the conversion of the initial script-based implementation into a modular, object-oriented design. The refactor aimed to improve code organization, readability, and maintainability by encapsulating related functionalities into classes and separating concerns into different modules.

 Objectives

- **Modularity:** Divide the project into modular components, each responsible for a specific functionality.
- **Object-oriented design:** Utilize classes and objects to encapsulate related data and behaviors.
- **Code organization:** Organize the project structure to enhance readability and maintainability.
- **Separation of concerns:** Decouple different functionalities to improve code clarity and reusability.

 Changes Made

1. **Creation of Classes:**
    - Identified distinct functionalities in the initial script and encapsulated them into individual classes.
    - Defined classes for WebcamCapture, OCR, Gemini, NotificationSender, MessageSender, and CurrencyDetection.
2. **Module Separation:**
    - Split the project into separate modules, each containing related classes and functions.
    - Modules include capture, ocr, gemini, notification, message, and currency_detection.
3. **Code Refactoring:**
    - Refactored the initial script to utilize the newly created classes and modules.
    - Organized the code into logical sections within each class, following best practices for code readability.
4. **Dependency Management:**
    - Ensured proper dependency management by importing required libraries within each module.
    - Utilized virtual environments or package managers to manage dependencies and versioning.
5. **Documentation:**
    - Documented each class and module, outlining its purpose, functionalities, and usage.
    - Provided inline comments and docstrings to clarify code intent and usage.

 Benefits

- **Improved Readability:** The modular structure and object-oriented design make the code more readable and understandable.
- **Enhanced Maintainability:** Changes or updates to specific functionalities can be made within their respective classes or modules without affecting other parts of the codebase.
- **Reusability:** Encapsulating functionalities into classes promotes code reuse, allowing similar tasks to be easily implemented in different contexts.
- **Scalability:** The organized structure facilitates the addition of new features or functionalities in the future without significant code restructuring.

 Conclusion

The refactoring process successfully transformed the initial script-based implementation of the SixthSense_Gdsc project into a well-organized, modular codebase. By leveraging classes and modules, the project now offers improved readability, maintainability, and scalability. The separation of concerns and encapsulation of functionalities into classes lay a solid foundation for future development and expansion of the project.

---

### 1.4. Gemini

 Overview

This documentation outlines the conversion of the original code for optimization purposes, focusing on reducing content size and improving retrieval speed. The primary objectives of this conversion are to streamline the codebase, minimize redundant operations, and enhance overall performance.


 Changes Made

1. **Class Segmentation**:
2. **Introduction of Assistant Class**:
3. **Output Formatting**:

 Optimization Strategies

1. **Content Size Reduction**:
2. **Speed Optimization**:

 Performance Evaluation

1. **Content Size Reduction**:
2. **Speed Optimization**:

 Conclusion

The conversion of the code for optimization purposes aims to enhance both content size and retrieval speed. By segmenting the code into classes, limiting response length, and introducing streamlined processing, the refactored version achieves better efficiency and performance. Ongoing monitoring and evaluation will ensure continued optimization and responsiveness.

---
### 1.5. Multiprocessing using ProcessPoolExecutor

 Overview

The multiprocessing library in Python provides support for parallelizing tasks across multiple CPU cores or processes. It offers several classes and functions to create and manage concurrent processes, improving efficiency and performance in multiprocessing environments.
![threading](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/threading.png)
 ProcessPoolExecutor

The **`ProcessPoolExecutor`** is a high-level interface provided by the concurrent.futures module, built on top of the multiprocessing library. It enables concurrent execution of multiple tasks or functions within separate processes, allowing for parallelism and efficient resource utilization.

 Usage

1. **Initialization**:
    - The **`ProcessPoolExecutor`** is initialized with the desired maximum number of worker processes (**`max_workers`**).
    - `with ProcessPoolExecutor(max_workers=2) as ex:`
2. **Submit Tasks**:
    - Tasks or functions are submitted for execution using the **`submit`** method.
    - `future1 = ex.submit(object_Detection) future = ex.submit(hi)`
3. **Retrieve Results**:
    - The **`submit`** method returns a **`Future`** object representing the result of the submitted task.
    - Results can be retrieved synchronously using the **`result`** method of the **`Future`** object.
    - `result1 = future1.result() result2 = future.result()`
4. **Completion**:
    - The main process waits for the completion of all submitted tasks before proceeding further.
    - `future1.result() future.result()`

 Dependencies

- Python multiprocessing library
- concurrent.futures module

 Notes

- Ensure that tasks submitted to the **`ProcessPoolExecutor`** are designed to be parallelizable and do not rely on shared state or resources that might lead to race conditions.
- Experiment with different values for **`max_workers`** to find the optimal number of worker processes based on system specifications and workload characteristics.

 Conclusion

In summary, the multiprocessing library, coupled with the ProcessPoolExecutor, offers a convenient approach for concurrent task execution in Python, enhancing performance by utilizing multiple CPU cores. By judiciously configuring the executor and task distribution, developers can optimize resource utilization and improve application responsiveness, contributing to efficient parallel processing.

### 1.6. Voice Assistant

 **Introduction**

This documentation outlines a Python script for a speech recognition assistant that listens for specific wake words and responds to user speech using text-to-speech conversion. The script utilizes various libraries for speech recognition and audio manipulation.
![speech to speech](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/speech%20to%20speech.png)
 **Imports**

The script imports the following libraries:

- **`speech_recognition`** (**`sr`**): Recognizes speech from audio recordings.
- **`pyaudio`**: Interacts with the computer's audio hardware for recording.
- **`os`**: Interacts with the operating system.
- **`time`**: Provides timing functionalities.
- **`playsound`**: Plays audio files on the system.
- **`gtts`**: Converts text to speech and saves it as an audio file.

 **GTTS Function**

- **`GTTS(text)`**: Converts text to speech and plays the generated audio using **`playsound`**.

 **get_audio Function**

- **`get_audio()`**: Captures user speech and converts it to text using the **`Recognizer`** instance from **`speech_recognition`**. It listens for audio input from the microphone, records audio, and attempts to recognize the spoken words using Google Speech-to-Text.

 **Main Function**

- **`main()`**: Entry point of the program. Calls **`get_audio()`** to capture and recognize user speech. It then checks if the recognized text contains the wake word "hello". If found, responds with "Hey, how are you?" using **`GTTS`**.

 **Wake Word and Loop**

- **`WAKE = "hello everyone"`**: Defines the wake word that triggers the assistant.
- The script enters a loop that continuously listens for audio using **`get_audio()`**. If the wake word is detected, the assistant responds and listens for further instructions.

 **Usage**

To use the speech recognition assistant, run the script and wait for the prompt. Speak the wake word "hello everyone" to trigger the assistant, then give instructions or ask questions as needed.

### 1.7. Google Calendar API

**Introduction**

This documentation outlines a Python script that integrates with the Google Calendar API to provide virtual assistant functionalities, including accessing calendar events and creating notes using speech recognition and text-to-speech.

**Imports**

- Standard library imports: **`datetime`**, **`pickle`**, **`os`**, **`time`**
- Google Calendar API imports: **`build`** from **`googleapiclient.discovery`**, **`Credentials`**, and **`InstalledAppFlow`** from **`google_auth_oauthlib.flow`**
- Speech recognition and Text-to-Speech (TTS) imports: **`sr`** for speech recognition, **`pyttsx3`**, and **`gTTS`** for text-to-speech
- Other imports: **`playsound`** for playing audio files, **`subprocess`** for opening external applications

**Google Calendar Authentication**

- **`SCOPES`**: Defines the permissions required to access Google Calendar data.
- **`create_service(client_secret_file, ...)`**: Function to create a service object for interacting with the Google Calendar API. It handles OAuth2 authentication and stores credentials for future use.

 **Helper Functions**

- **`convert_to_RFC_datetime(year, month, day, hour, minute)`**: Converts date and time information to a format compatible with the Google Calendar API.
- **`speak(text)`**: Converts text to speech and plays the audio using either **`pyttsx3`** or **`gTTS`**.

**Voice Class**

- Provides methods for speech recognition and interaction with the virtual assistant:
    - **`get_audio()`**: Listens for user input and converts it to text using **`sr`** (SpeechRecognition).
    - **`authenticate_google()`**: Function for an alternative authentication approach (currently commented out).
    - **`get_events(day, service)`**: Retrieves calendar events for a specific day using the Google Calendar service object.
    - **`get_date(text)`**: Parses user's spoken text to extract date information in various formats.
    - **`note(text)`**: Creates a text file with the provided note text and opens it using **`notepad.exe`** (Windows specific).

 **Main Loop**

- **`WAKE = "hello"`**: Defines the wake word to activate the virtual assistant.
- **`SERVICE = authenticate_google()`**: Calls the authentication function.
- The script continuously listens for user input:
    - Captures user's spoken command.
    - Processes the command based on keywords related to calendar and note functionalities.
    - If no matching keywords are found, responds with "I don't understand".

 **Conclusion**

This documentation provides an overview of a Python script that integrates with the Google Calendar API to create a virtual assistant capable of accessing calendar events and creating notes using speech recognition and text-to-speech functionalities.

### 1.8. Distance Warning system using Midas 2.1V small

**Introduction:**
The Depth Estimation module, powered by the MIDAS (Monocular Depth Estimation in Real-Time with Deep Learning on Large-Scale Datasets) model, incorporates a Distance Warning System to assist visually challenged individuals in navigation. This addendum outlines the implementation, benefits, and impact of the distance warning system in conjunction with depth estimation.

**Implementation:**
The Distance Warning System is integrated into the existing depth estimation workflow. Upon estimating depth from input images using the MIDAS model, the system analyzes the depth map to identify obstacles in proximity. If an object is detected within a predefined threshold distance, the system triggers an alert to warn the individual about the obstacle's presence.

**Benefits of the Distance Warning System:**

1. **Enhanced Safety:** The Distance Warning System enhances safety for visually challenged individuals by providing real-time alerts about nearby obstacles, enabling them to navigate with increased awareness and confidence.
2. **Independence:** By providing timely warnings, the system promotes independence and autonomy for visually challenged individuals, empowering them to navigate environments with reduced reliance on assistance.
3. **User-Friendly Interface:** The system offers a user-friendly interface, delivering audible or tactile alerts that are easily perceivable and actionable by individuals with visual impairments.

**Impact and Use Cases:**

1. **Indoor Navigation:** The Distance Warning System facilitates indoor navigation for visually challenged individuals, enabling them to maneuver through spaces such as homes, offices, and public buildings with greater ease and safety.
2. **Outdoor Mobility:** In outdoor environments, the system assists individuals in navigating sidewalks, pedestrian crossings, and other urban settings, reducing the risk of collisions with obstacles and hazards.
3. **Public Transportation:** When accessing public transportation services, the system helps individuals locate boarding points, navigate platforms, and avoid obstacles in transit stations.

**Integration with our Sixth Sense:**

The Distance Warning System has been  integrated with our Sixth Sense to provide seamless access and enhanced functionality. By leveraging existing  technologies in Sixth Sense, the system can reach a wider user base and integrate with other accessibility features.

**Conclusion:**

The integration of the Distance Warning System with the Depth Estimation module leveraging the MIDAS model represents a significant advancement in assistive technology for visually challenged individuals. By combining real-time depth estimation with proactive obstacle detection and warning capabilities, the system contributes to improved mobility, independence, and safety in navigating diverse environments.

### 1.9 Gemini and gemma
     Introduction

Our project integrates two powerful models, **Gemini** and **Gemma**, to provide assistance to visually impaired individuals. When online connectivity is available, Gemini is initiated to answer questions and provide information effectively. However, in situations where online connectivity is not established, Gemma seamlessly takes over to ensure uninterrupted assistance. This dynamic integration ensures continuous support for visually impaired individuals, regardless of their internet connection status. Additionally, our solution incorporates **Gemini Vision**, enabling users to explore their environment effectively. With Gemini Vision, users can inquire about objects or obstacles in front of them simply by asking questions. Furthermore, users have the ability to take a photo of their surroundings and ask questions about the captured image, enhancing their understanding and interaction with the world around them. This comprehensive approach to accessibility aims to empower visually challenged individuals by providing them with tools to access information, navigate their environment, and interact with their surroundings confidently and independently.
![](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/gemini%20pro%20gemma.png)
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
  1.10 ### Emotional Detection:
   

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
1.11 ### Gesture Recognition: 
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

This workflow incorporates object detection based on hand gestures, utilizing a TensorFlow Lite model for efficient inference on our device. Object detection is initiated only when a closed hand gesture is recognized, ensuring that system resources are utilized judiciously based on the user's gestures.

### 1.12 Face Distance Calculation

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
    - Return the calculated distance.
  
### 1.13 Object Detection:


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
## 2 Software

![caregiver app](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/threading.png)

### 2.1 Geofencing

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

### 2.2 Messaging 

Domain
React native - Mobile App
**Messaging Feature Overview**

1. **Previous Functionality**: Initially, blind users could send messages using voice commands like "Send Message," which would be sent to the caregiver app.
2. **Updated Messaging Tab**: Now, there's a dedicated messaging tab within the app where caregivers can type and send messages directly to blind users.
3. **Text-to-Speech Conversion**: Messages received by blind users are read aloud using machine learning models that convert text to speech specifically tailored for them.
4. ![message](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/Message.png)
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

### 2.3 Multi Language Support 

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


### Contact 

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
## 3 Hardware
### 3.1 Fall Detection 
![](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/gdsc/alert.png)
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


### 3.2 **Vibration Motor: Enhancing Safety Measures**

In the realm of safety measures, the vibration motor emerges as a crucial component to alert users promptly in various scenarios, such as detecting obstacles or receiving notifications from caregivers.

 **Introduction**

Vibration motors are compact devices designed to generate vibrations when powered, making them ideal for alert systems. These motors are particularly useful in situations where audible alarms might not be practical or when users need discreet notifications.

 **Understanding the DC Vibration Motor Module**





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

### 3.3 TPU (Tensor Processing Unit)

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

Different TPU and board benchmark of MobileNet v1 and MobileNet v2 model inference speed.



Power consumption of different board and coral TPU

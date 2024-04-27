import pyaudio
import webrtcvad
from voice_inference import Wave2Vec2Inference
import numpy as np
import threading
import time
import pyttsx3
from sys import exit
from queue import Queue

class VoiceAssistant:
    exit_event = threading.Event()

    def __init__(self, model_name="jonatasgrosman/wav2vec2-large-xlsr-53-english", device_name="default"):
        self.model_name = model_name
        self.device_name = device_name
        self.asr_output_queue = Queue()
        self.asr_input_queue = Queue()
        self.asr_process = threading.Thread(target=self.asr_process, args=(
            self.model_name, self.asr_input_queue, self.asr_output_queue,))
        self.vad_process = threading.Thread(target=self.vad_process, args=(
            self.device_name, self.asr_input_queue,))
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', self.tts_engine.getProperty('rate') - 15)
        self.tts_engine.setProperty('volume', self.tts_engine.getProperty('volume') + 1)

    def stop(self):
        """Stop the ASR and TTS processes"""
        VoiceAssistant.exit_event.set()
        self.asr_input_queue.put("close")
        print("ASR and TTS stopped")

    def start(self):
        """Start the ASR and TTS processes"""
        self.asr_process.start()
        time.sleep(5)  # Start VAD after ASR model is loaded
        self.vad_process.start()

    def asr_process(self, model_name, in_queue, output_queue):
        wave2vec_asr = Wave2Vec2Inference(model_name, use_lm_if_possible=False)

        print("\nListening to your voice\n")
        while True:
            audio_frames = in_queue.get()
            if audio_frames == "close":
                break

            float64_buffer = np.frombuffer(
                audio_frames, dtype=np.int16) / 32767
            start = time.perf_counter()
            text, confidence = wave2vec_asr.buffer_to_text(float64_buffer)
            text = text.lower()
            inference_time = time.perf_counter() - start
            sample_length = len(float64_buffer) / 16000  # Length in seconds
            if text != "":
                output_queue.put([text, sample_length, inference_time, confidence])

    def vad_process(self, device_name, asr_input_queue):
        vad = webrtcvad.Vad()
        vad.set_mode(1)

        audio = pyaudio.PyAudio()
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        # A frame must be either 10, 20, or 30 ms in duration for webrtcvad
        FRAME_DURATION = 30
        CHUNK = int(RATE * FRAME_DURATION / 1000)

        microphones = self.list_microphones(audio)
        selected_input_device_id = self.get_input_device_id(
            device_name, microphones)

        stream = audio.open(input_device_index=selected_input_device_id,
                            format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

        frames = b''
        while True:
            if VoiceAssistant.exit_event.is_set():
                break
            frame = stream.read(CHUNK, exception_on_overflow=False)
            is_speech = vad.is_speech(frame, RATE)
            if is_speech:
                frames += frame
            else:
                if len(frames) > 1:
                    asr_input_queue.put(frames)
                frames = b''
        stream.stop_stream()
        stream.close()
        audio.terminate()

    def get_input_device_id(self, device_name, microphones):
        for device in microphones:
            if device_name in device[1]:
                return device[0]

    def list_microphones(self, pyaudio_instance):
        info = pyaudio_instance.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')

        result = []
        for i in range(0, numdevices):
            if (pyaudio_instance.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                name = pyaudio_instance.get_device_info_by_host_api_device_index(
                    0, i).get('name')
                result += [[i, name]]
        return result

    def get_audio(self):
        """Returns the text, sample length, and inference time in seconds."""
        text, _, _, confidence = self.asr_output_queue.get()
        return text

        

    def speak(self, text):
        """Speak the given text using the TTS engine"""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

# if __name__ == "__main__":
#     print("Voice Assistant")
#     assistant = VoiceAssistant()
#     assistant.start()

#     try:
#         while True:
#             text = assistant.get_audio()
#             # print(f"{text}")
#             print(text)
#             assistant.speak(text)

#     except KeyboardInterrupt:
#         assistant.stop()
#         exit()
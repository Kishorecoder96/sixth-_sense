import PIL.Image
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import google.api_core.exceptions
import google.protobuf.json_format
import google.api_core.exceptions

api_key = "Api-Key"
genai.configure(api_key=api_key)

class GeminiProAssistant:
    def __init__(self, voice_assistant):
        self.voice_assistant = voice_assistant
        self.llm = ChatGoogleGenerativeAI(google_api_key=api_key, model='gemini-pro', temperature=0.5)
        self.output_parser = CommaSeparatedOutput()
        self.system_template = """
        You are a helpful AI assistant created to assist visually impaired users. 
        When the user asks a question, provide a concise and informative response in about 20 words.
        """
    def respond(self, question):
        try:
            self.human_template = "{text} + give me in most concise manner"
            self.chat_prompt = ChatPromptTemplate.from_messages([
                ("system", self.system_template), 
                ("human", self.human_template)
            ])
            self.chain = self.chat_prompt | self.llm | self.output_parser
            response = self.chain.invoke("{text: " + question + " }")
            if response:
                self.voice_assistant.speak(response)
            else:
                self.voice_assistant.speak("Sorry, can't answer that question.")
        except (google.protobuf.json_format.ParseError, AttributeError) as e:
            self.voice_assistant.speak("Sorry an unknowed error occured")
            raise google.api_core.exceptions.BadRequest(
                "Unknown error trying to retrieve streaming response. "
                "Please retry with `stream=False` for more details."
            )
        except Exception as e:
            self.voice_assistant.speak("Sorry an Error occurred")


class CommaSeparatedOutput(BaseOutputParser):
    def parse(self, text: str):
        words = text.strip().split(",")
        return ", ".join(words[:4])


class GeminiVisionProAssistant:
    def __init__(self, voice_assistant, gemini_pro_vision=genai.GenerativeModel('gemini-pro-vision')):
        self.voice_assistant = voice_assistant
        self.gemini_pro_vision = gemini_pro_vision

    def trigger_gemini_vision_pro(self, image_path,
                                  question="Reply to the question in a most concise manner with identifying the minute details in the image"):
        try:
            if image_path:
                image = PIL.Image.open(image_path)
                image_resized = image.resize((128, 128))
                input_prompt = """
                You are a caregiving assistant for a blind person.
                You have to describe the image briefly and accurately.
                Generate the right answer.
                You have to guide him through the way.
                """
                response = self.gemini_pro_vision.generate_content(
                    [input_prompt + question + "Give me in a most concise manner", image_resized])
                text_output = response.text
                if text_output:
                    self.voice_assistant.speak(text_output)
                else:
                    self.voice_assistant.speak("Sorry, I can't answer that question.")
            else:
                self.voice_assistant.speak("No image provided.")
        except (google.protobuf.json_format.ParseError, AttributeError) as e:
            self.voice_assistant.speak("Sorry an unknowed error occured")
           
            raise google.api_core.exceptions.BadRequest(
                "Unknown error trying to retrieve streaming response. "
                "Please retry with `stream=False` for more details."
            )
        except Exception as e:
            self.voice_assistant.speak("Sorry an error occurred")

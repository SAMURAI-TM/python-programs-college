import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize speech recognition, text-to-speech engine, and translator
recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language="hi-IN")
            return text.lower()
        except sr.UnknownValueError:
            print("क्षमा करें, मुझे समझ में नहीं आया।")
            return ""
        except sr.RequestError as e:
            print(f"Error: {e}")
            return ""

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    user_input = recognize_speech()
    
    if "नमस्ते" in user_input:
        speak("नमस्ते! मैं आपकी किस प्रकार सहायता कर सकता हूं?")
    elif "तुम्हारा नाम क्या है" in user_input:
        speak("मेरा नाम असिस्टेंट है। आपकी सेवा में।")
    elif "अलविदा" in user_input:
        speak("अलविदा!")
        break
    else:
        translation = translator.translate(user_input, src='hi', dest='en')
        speak("मुझे क्षमा करें, मैं उसे समझ नहीं पाया। क्या आप कुछ और कहना चाहेंगे?")

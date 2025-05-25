import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import datetime
import webbrowser
import pyaudio
import os

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

# Function to speak a text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # To handle ambient noise
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")
        return ""

# Function to fetch the current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

# Function to fetch a random joke
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

# Function to search Wikipedia
def search_wikipedia(query):
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia: " + results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There were multiple results, could you be more specific?")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("Sorry, there was a problem with the Wikipedia service.")
    except Exception as e:
        speak("Sorry, I couldn't find any information on that topic.")

# Function to open a website
def open_website(query):
    webbrowser.open(query)
    speak(f"Opening {query}...")

# Main function to handle the AI commands
def main():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        query = listen()

        if 'hello' in query:
            speak("Hello, how can I assist you today?")
        
        elif 'time' in query:
            current_time = get_time()
            speak(f"The current time is {current_time}.")
        
        elif 'joke' in query:
            tell_joke()
        
        elif 'search' in query or 'wikipedia' in query:
            query = query.replace("search", "").replace("wikipedia", "")
            search_wikipedia(query)
        
        elif 'open' in query:
            query = query.replace("open", "").strip()
            open_website(query)
        
        elif 'exit' in query or 'goodbye' in query:
            speak("Goodbye! Have a great day.")
            break
        
        else:
            speak("Sorry, I didn't understand that. Please try again.")
        
if __name__ == "__main__":
    main()

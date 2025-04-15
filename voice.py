import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)

    try:
        print("Recognizing...")
        command = listener.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Could not request results. Check your internet.")
        return ""

def run_assistant():
    speak("How can I help you?")
    command = take_command()
    if 'hello' in command:
        speak("Hello there!")
    elif 'your name' in command:
        speak("I'm your Python voice assistant.")
    elif 'stop' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Please repeat your command.")

while True:
    run_assistant()
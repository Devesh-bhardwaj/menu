
import datetime
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Laaiila Version 1")
    speak("I am your Assistant")
    speak(assname)


def usrname():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome {}".format(uname))


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening to you ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return query

import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Crypto Jarvis. Sir Please tell me how may I Help You")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun Raha hun Tu Boll..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconnect Ho raha hun yarrr...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Na Kaha: {query}\n")

    except Exception as e:
        print(e)
        print("Phir sa bolo...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()
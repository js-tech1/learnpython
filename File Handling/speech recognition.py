import speech_recognition as sr 
import webbrowser
import numpy as np
import pyttsx3
# import pocketsphinx
import random,os
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',140)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume+0.50)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(s)
         a = r.listen(source)
         try:
        
                    return r.recognize_google(a)

         except sr.UnknownValueError:
                print('could not understand audio')

         except sr.RequestError as e:
                print("Recog Error; {0}".format(e))

         return ""

engine.say("How can i help you jeet sir!")
print ("how can i help you jeet sir!")
engine.runAndWait()
r = sr.Recognizer()

def search():
    with sr.Microphone() as source:
     a = r.listen(source)

    engine.say("opening" +user)
    print ("opening "+user)
    engine.runAndWait()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def online():
    speak('hello sir')
    print("hello sir")

def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize_google(audio)

    if user == "hi":
        online()
    
    elif user == "search":
        search()
    elif user == "down":
            gooffline()
    elif user == "shutdown":
            shutdown()
    elif user in ['hello','hey','whatsup','sup']:
        d = random.choice(['hey','hi','sup'])
        speak(d)
    elif user in ['you are fine']:
        speak(['i am finee jeet thakn you how you are'])
    elif user in ['i am fine',]:
        speak(['wonderful'])
        

if __name__ == "_main_":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
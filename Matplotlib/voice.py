import pyttsx3
from sklearn import preprocessing
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',140) #talk speed
volume = engine.getProperty('volume')
engine.setProperty('volume',volume+0.50) #for volum
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

while 1:
    a=str(input(" enter txt to speach :-"))
    engine.say(a)
    print (a)
    engine.runAndWait()
    
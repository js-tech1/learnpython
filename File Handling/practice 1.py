import os
import time
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',140)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume+0.50)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def clearConsole():
            if os.name in('nt','dos'):
                command='cls'
            os.system(command)


name = "Application"



try:
    z=os.mkdir(name)
except:
    os.chdir(name)
class page1:

    while (1):

            
        engine.say("enter your details")
        engine.runAndWait()
        fname = str(input("Enter First Name: "))
        lname = str(input("Enter Last Name: "))
        pcode = str(input("Enter Pincode: "))
        uname = str(input("Enter User Name: "))
        pawd = str(input("Enter Password: "))
        repd = str(input("Re-Enter Password: "))

        a = fname
        b = lname 
        c = pcode 
        d = uname 
        e = pawd 
        f = repd

        
        if(e == f):
                

            nm = (d+(".txt"))
            fp = open(nm,"a")
            fp.write("ACCOUNT DETAILS: ")
            fp.write("Your Name is: "+a+b)
            fp.write("\n")
            fp.write("Your Username is: "+d)
            fp.close()
            print(a,b,c,d,e,f)
            time.sleep(10)
            clearConsole()
            
        else:

            engine.say("password does not match")
            # engine.runAndWait()
            print("PASSWORD DOES NOT MATCH")

            engine.say("enter your details again")
            # engine.runAndWait()
            print("Enter Details Again")

            time.sleep(5)

            clearConsole()
                    

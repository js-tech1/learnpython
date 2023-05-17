from tkinter import *
import tkinter as Tk
import playsound
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

pc = Tk()
pc.title("PythonGuides")
pc.geometry('400x300')
pc['bg'] = '#5ea0c0'


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
    

    while(1):

            
        engine.say("enter your details")
        engine.runAndWait()
        z = Button(pc,text="Register Account",bg='black',fg='white',font='20', padx=10, pady=5).place(x=140,y=240)

        firstnameLabel = Label(pc, text="First Name", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
        firstname = StringVar()
        firstnameEntry = Entry(pc, textvariable=firstname,width='30').place(x=220,y=40)

        lastname = Label(pc, text="Last Name", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
        lastname = StringVar()
        lastnameEntry = Entry(pc, textvariable=firstname,width='30').place(x=220,y=40)

        pincodeLabel = Label(pc, text="Pin Code", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
        pincode = StringVar()
        pincodeEntry = Entry(pc, textvariable=firstname,width='30').place(x=220,y=40)

        usernameLabel = Label(pc, text="First Name", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
        username = StringVar()
        usernameEntry = Entry(pc, textvariable=firstname,width='30').place(x=220,y=40)


        passwordLabel = Label(pc, text="Password", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
        password = StringVar()
        passwordEntry = Entry(pc, textvariable=firstname,width='30').place(x=220,y=40)

        reenterLabel = Label(pc, text="Re-Enter Password", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
        reenter = StringVar()
        reenterEntry = Entry(pc, textvariable=firstname,width='30').place(x=220,y=40)


        pname = username.get()
        fsn = firstname.get()
        lsr = lastname.get()
        pcd = pincode.get()
        pwd = password.get()
        rpd = reenter.get()
        playsound.playsound('Click.wav',True)
        Label(pc, text=f'Your Username is:{pname}\n Your Name is: {fsn} {lsr} \n{pcd} \n{pwd}', pady=20, bg='#5ea0c0',fg='black', font=20).place(x=115, y=310)



        




        if(pwd == rpd):
                

            nm = (pname+(".txt"))
            fp = open(nm,"a")
            fp.write("ACCOUNT DETAILS: ")
            fp.write("Your Name is: "+fsn+lsr)
            fp.write("\n")
            fp.write("Your Username is: "+pname)
            fp.close()
            clearConsole()
            
        else:

            engine.say("password does not match")
            engine.runAndWait()
            print("PASSWORD DOES NOT MATCH")

            engine.say("enter your details again")
            engine.runAndWait()
            print("Enter Details Again")

            time.sleep(5)


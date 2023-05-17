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

name=str(input("Enter Folder Name: "))
# os.mkdir(name)
os.chdir(name)
try:
    a=os.mkdir("joe")
except:
    print("\nFolder Already Exists\n")
    engine.say("folder already exist.....")
    engine.runAndWait()
        
    print("Please Try With Another Name or Delete the Existing Folder ")
    engine.say("select option .....")
    engine.runAndWait()
        
    print(input("press 'y' to delete\n press 'n' to create new folder"))
    a= input(str)
    if(a=='y'):

        engine.say("please wait.....")
        engine.runAndWait()
        engine.say("your file is deleting.....")
        engine.runAndWait()
        

        
        b=os.rmdir("joe") 
        print("\n Deleting Folder\n")
        time.sleep(2)
        print("Folder Deleted Successfully")
        a==b
        engine.say("deleted successfully.....")
        engine.runAndWait()
        
    
    elif(a=='n'):
            namee=str(input("Enter Folder Name: "))
            os.mkdir(namee)

            engine.say("creating new folder.....")
            engine.runAndWait()
            engine.say("please wait.....")
            engine.runAndWait()
            
            print("folder with title" +(" ") +namee +(" ")+ ("Folder Created Successfully"))

            engine.say("folder created successfully.....")
            engine.runAndWait()

    else:
        print("please enter correct output")
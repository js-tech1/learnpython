import os
# import sum
import loading 
from time import sleep, time
from sum import *


def clearConsole():
            if os.name in('nt','dos'):
                command='cls'
            os.system(command)

def nrl(a,b,c,x,y):
    
    print("Your Account Created Successfully")

    print("_________________________________")
    print("\nHello Mr.",a.title(),b.title())
    print("_________________________________")
    print("\n First Name: ",a.title())
    print("\n Surname: ",b.title())
    print("\n Pincode: ",c)

    def imp(x,y):

        print("_________________________________")
        print("\nImportant Data:")
        print("_________________________________")
        print("\n Username: ",x)
        print("\n Password: ",y)

    imp(x,y)
a=str(input("Enter Your Name: "))
b=str(input("Enter Your Surname: "))
c=str(input("Enter Your Pincode: "))


x=str(input("Username: "))
y=str(input("Password: "))

clearConsole()

loading.load()


nrl(a,b,c,x,y)
f= input("press enter to continue:")
if(f):
   std()

clearConsole()

ins()


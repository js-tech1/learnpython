import os
import time
import playsound
while(1):
    def clearConsole():
        if os.name in('nt','dos'):
            command='cls'
        os.system(command)
    def displayIntro():
    	playsound.playsound('atml.wav',True)
while(1):
        a=str(input("Enter Your Name: "))
        res = True if next((chr for chr in a if chr.isdigit()), None) else False
        
        if res == True:
            print("Only Charcters Allowed")
        else:
            print(" ")
            break
b=str(input("Enter Your Surname: "))
print(a,b)

c=int(input("Enter Area Pin code: "))
lo=0
print("Account Created Successfully")

print(a,b)    
Run=str(input("\nYou want to continue Y or N: "))
 
if(Run=="Y" or Run=="y"):
        print(" ")
        clearConsole()
         
if(Run=="N" or Run=="n"):
    break
while( lo<3):
        lo=lo+1
        d=int(input("Enter Card Pin: "))
        e=int(input("Re Enter Card Pin: "))
        if(d==e):
            print("Your Account Details Are Saved")


        if(d==e):
            F=int(input("Enter Amount: "))
            print("please wait...")
            time.sleep(2)
            print("please wait...")
            time.sleep(2)
            print("please wait...")
            time.sleep(2)
            print("please wait...")
            time.sleep(2)
            print("please wait...")
            time.sleep(2)
            print("please wait...")
            time.sleep(2)
            print("Please Wait...")
            displayIntro()
            
            break
        
else:
        print("enter again")
        clearConsole()
    

Run=str(input("Thank you for using ABC ATM, Do you want to continue or proceed again"))
 
if(Run=="Y" or Run=="y"):
         print(" ")
clearConsole()
         
if(Run=="N" or Run=="n"):
    break

Run=str(input("Thank you for using ABC ATM"))
if(Run==Run):
    break
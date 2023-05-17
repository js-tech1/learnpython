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

        c=int(input("Enter Area Pin code: "))
        lo=0
        print("Account Created Successfully")
 
        Run=str(input("\nYou want to continue Y or N: "))
    
        if(Run=="Y" or Run=="y"):
            res = True if next((chr for chr in a if chr.isdigit()), None) else False
        else:
            print(input("Enter Y or N only: "))
            clearConsole()
            
        if(Run=="N" or Run=="n"):
            break
        while( lo<3):
            lo=lo+1
            d=int(input("Enter Card Pin: "))
            e=int(input("Re Enter Card Pin: "))
            if(d==e):
                print("Your Account Details Are Saved")

                print('Please Press 1 For Your Bank Balance: \n')
                print('Please Press 2 To Make a Withdrawl: \n')
                print('Please Press 3 To Make a Deposit: \n')
                print('Please Press 4 To Fast Cash: \n')
                option = int(input('Enter Your Request: '))
                if  option == 1:
                    print('Your Balance is:  ',10000,'\n')
            

                    restart = input('Would You you like to go back?: ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
                elif option == 2:
                    option2 = ('y')
            while():
                if(d==e):
                    F=int(input("Enter Amount: "))
                elif ('Balance==10000'):
                    print("You don't have sufficient balance")
                    
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
            
                    restart = input('Would You you like to go back?: ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
                if option == 3:
                    option3 = ("y")
                    print(input("How much you want to deposit: "))
                if option == 4:
                    option4 = ("y")
                    print("Enter 100: /n")
                    print("Enter 500: /n")
                    print("Enter 1000: /n")
                    print("Enter 5000: /n")
                    print("Enter 10000: /n")

            Run=str(input("Thank you for using ABC ATM, Do you want to continue or proceed again"))
        
            if(Run=="Y" or Run=="y"):
                print(" ")
            clearConsole()
                
        if(Run=="N" or Run=="n"):

            Run=str(input("Thank you for using ABC ATM"))
            if(Run==Run):
                break
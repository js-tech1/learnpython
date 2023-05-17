import os
from nested import nrl

def clearConsole():
            if os.name in('nt','dos'):
                command='cls'
            os.system(command)

def std(a,b,c,d,e):
    
    sum = a+b+c+d+e
    clearConsole()
    print("Your Total is: ",sum,"/500")
    percentage = (sum/500.0)*100
    print("Your Percentage is: ",percentage, "%")


    kk=(input("press enter to calculate again: "))
    clearConsole()
    if kk==1:
        nrl()
    else:
        ins()

def ins(): 
    while(1):
        
        a=int(input("Maths: "))
        
        if(a>100):
            print("Error: Please Enter marks Under 100!")
        else:break
    while(1):
        
        b=int(input("Chemistry: "))
        
        if(b>100):
            print("Error: Please Enter marks Under 100!")
        else:break
    while(1):
        
        c=int(input("Physics: "))
        
        if(c>100):
            print("Error: Please Enter marks Under 100!")
        else:break

    while(1):
        
        d=int(input("Computer: "))
        
        if(d>100):
            print("Error: Please Enter marks Under 100!")
        else:break
    while(1):
        
        e=int(input("English: "))
        
        if(e>100):
            print("Error: Please Enter marks Under 100!")
        else:break


    input("press enter to generate: ")  
    
    clearConsole()
    std(a,b,c,d,e)

    
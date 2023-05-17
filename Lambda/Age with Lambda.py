while(1):
    a = int(input("Enter Your Age: "))
    
    b = lambda a: a >= 18
    nn=(b(a))           #create a new fuinction
    if (nn==True):
        
        print("You are Eligible")

    else:
        print("Your are not Eligible")
"""
def jack(a):
    a>18
    #for backend work without lambda
"""
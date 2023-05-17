while(1):
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    gg = input("Enter choice: ")

    sums = lambda x,y,k: x+y if(k =='+') else None
    print(sums(a,b,gg))

    minus = lambda x,y,k: x-y if(k =='-') else None
    print(minus(a,b,gg))

    multiply = lambda x,y,k: x*y if(k =='*') else None
    print(multiply(a,b,gg))

    divide = lambda x,y,k: x/y if(k =='/') else None
    print(divide(a,b,gg))
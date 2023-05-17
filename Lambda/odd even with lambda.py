while(1):
    num = lambda x:1 if x%2 == 0 else 0
    print("Enter Number to Check")
    if(num(int(input()))):
        print("Even")
    else:
        print("Odd")

while(1):

    v1 = int(input("Enter Number 1: "))
    v2 = int(input("Enter Number 2: "))


# x and y is parameters
    sums = (lambda x,y:x+y)
    print(sums(v1,v2))

    multi = (lambda x,y:x*y)
    print(multi(v1,v2))

    divide = (lambda x,y:x/y)
    print(divide(v1,v2))

    minus = (lambda x,y:x-y)
    print(minus(v1,v2))
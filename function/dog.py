class Dog():
    

    def __init__(jack, name, age):
        jack.name = name
        jack.age = age
        
    def sit(jack):

        print(jack.name.title() + " is now sitting.")
        print(jack.age)

    def roll_over(jack):

        print(jack.name.title() + " rolled over!")
        print(jack.age)

a=str(input("enter name"));
b=int(input("enter age"));      
p1=Dog(a,b)
    # p2=Dog(input("enter age"))

p1.sit()
    # p2.sit()

p1.roll_over()
    # p2.roll_over()
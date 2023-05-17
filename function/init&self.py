class Dog():
    

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def sit(self):

        print(self.name.title() + " is now sitting.")
        print(self.age)

    def roll_over(self):

        print(self.name.title() + " rolled over!")
        print(self.age)
a=str(input("enter name"));
b=int(input("enter age"));      
p1=Dog(a,b)

""" 
***method 2***
p1=Dog(str(input("enter name")),int(input("enter age")))"""

p1.sit()
# p2.sit()

p1.roll_over()
# p2.roll_over()
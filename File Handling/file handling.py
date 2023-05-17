import os

name = str(input("Enter Your Name: "))
f = str(input("Enter Your ID: "))

c = (name+(".txt"))
b = open(c,"a")
b.write("Your Name is: "+name)
b.write("\n")
b.write("Your ID is: "+f)
b.close()

os.remove("malhar.text")
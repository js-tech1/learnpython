from ast import Return


a=int(input())
exp=10
rate = lambda T : Return(200*exp(-T)) if (T>200)  else Return(400*exp(-T))
print(rate(a))
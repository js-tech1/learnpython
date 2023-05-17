# num = 10
# for i in range (1,10):
#     num.append(i)
#     even = filter(lambda n: n%2 == 0,num)
#     odd = filter(lambda n: n%2 == 1,num)

#     print(list(even))
odd=(lambda ii: ii%2==0)
even=(lambda k: k%2==1)


for i in range(10):
     print(odd(i))
     print(even(i))



# a = int(input("Enter start number: "))
# b = int(input("Enter last number: "))

# for num in range(10):
#     run=(lambda x: print(x,"even")if(num%2==0) else print(x,"odd"))
#     print(run(num))
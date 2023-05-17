jack = {1: "ja", 2: "ck"}
print("how many data you want to enter")
kk = int(input("enter number: "))
ll = 0
while ll < kk:
        ll += 1
        qq = int(input("enter data number: "))
        rr = input("enter value: ")
        vv = input("re enter value: ")
        jack[qq] = rr
        if(rr==vv):
            print("VALUE IS CORRECT")
        else:
            print("VALUE DOES NOT MATCH")
            print("entere again")
        break
check = int(input("enter number: "))
print(jack[check])
run=str(input("do you want to delete a value:"))
if(run=="y"):
    print(input("enter the value you want to delete: "))
    print("value is deleted")
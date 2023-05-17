import os
from time import sleep
import sum

def load():
    msg = 11
    for x in range(1):
        msg = msg-1
        print(msg)
        sleep(1)
        os.system("cls")

    print("Done!")

    h= input("press enter to continue: ")
    if(h):
        sum.ins()


   

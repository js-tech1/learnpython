from tkinter import *

from asyncio.windows_events import NULL
import os
import time

pc = Tk()
pc.title("PythonGuides")
pc.geometry('400x300')
pc['bg'] = '#5ea0c0'

def cc():
    if os.name in('nt','dos'):
        command='cls'
    os.system(command)


def gv():
    qq=vl1.get()
    ww=vl2.get()
    Label(pc, text=f'{qq}{ww}', pady=20, bg='#5ea0c0',fg='black', font=20).pack()
    # chk=(data(qq,ww))

    # if chk == True:
    #     Label("a is big")
    # elif chk == False:
    #     Label("b is big")
    # else:
    #     print("equal")

    # time.sleep(5)    

    # cc()

    


vl1Label=Label(pc,text="Enter Number 1: ", bg='#5ea0c0', fg='#b00d4c',font='20').pack()
vl1 = StringVar()
vl1Entry = Entry(pc, textvariable=vl1,width='30').pack()

vl2Label=Label(pc,text="Enter Number 2: ", bg='#5ea0c0', fg='#b00d4c',font='20').pack()
vl2 = StringVar()
vl2Entry = Entry(pc, textvariable=vl2,width='30').pack()


Button(pc,text="Register",bg='black',fg='white',font='20', padx=10, pady=5,command=gv()).pack()
    
    

pc.mainloop()


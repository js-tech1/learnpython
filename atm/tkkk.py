from re import L
from struct import pack
from tkinter import *

ws = Tk()
ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#5ea0c0'

def printValue():
    pname = username.get()
    fsn = firstname.get()
    lsr = lastname.get()
    pcd = pincode.get()
    pwd = password.get()
    rpd = reenterpassword.get()


    if(pwd==rpd):
        Label(ws, text=f'Your Username is: {pname} \n Your Name is: {fsn} {lsr} \n{pcd} \n{pwd}', pady=20, bg='#5ea0c0', fg='black').pack()
    else:
        Label(ws, text=f'Password does not match', pady=20, bg='#5ea0c0', fg='black').pack()

firstnameLabel = Label(ws, text="First Name", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=37)
firstname = StringVar()
firstnameEntry = Entry(ws, textvariable=firstname,width='30').place(x=220,y=40)


lastnameLabel = Label(ws, text="Last Name", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=72) 
lastname = StringVar()
lastnameEntry = Entry(ws, textvariable=lastname,width='30').place(x=220,y=78)


usernameLabel = Label(ws, text="User Name", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=0)
username = StringVar()
usernameEntry = Entry(ws, textvariable=username,width='30').place(x=220,y=5)


pincodeLabel = Label(ws, text="Pin Code", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=110)
pincode = StringVar()
pincodeEntry = Entry(ws, textvariable=pincode,width='30').place(x=220,y=118)


passwordLabel = Label(ws, text="Password", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=150)
password = StringVar()
passwordEntry = Entry(ws, textvariable=password, show="*",width='30').place(x=220,y=160)

reenterpasswordLabel = Label(ws, text="Re-enter Password", bg='#5ea0c0', fg='#b00d4c',font='20').place(x=30,y=195) 
reenterpassword = StringVar()
reenterpasswordEntry = Entry(ws, textvariable=reenterpassword, show="*",width='30').place(x=220,y=200)


Button(ws,text="Register Player",bg='black',fg='white',font='20', padx=10, pady=5,command=printValue).place(x=140,y=240)

ws.mainloop()
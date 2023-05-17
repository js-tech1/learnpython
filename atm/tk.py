from tkinter import *


ws = Tk()
ws.title("atm mashine")
ws.geometry('500x500')
ws['bg'] = '#28917c'

def printValue():
    pname = player_name.get()
    Label(ws, text=f'{pname}, Registered!', pady=20, bg='#28917c', fg='red').pack()

player_name = Entry(ws)
player_name.pack(pady=30)
Button(ws,text="Register Player", padx=10, pady=5,command=printValue).pack()

ws.mainloop()
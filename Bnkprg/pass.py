from tkinter import *

root = Tk()
root.title("PythonGuides")
root.geometry('400x300')
root['bg'] = '#5ea0c0'



def mach():
    As = Tk()
    As.title("PythonGuides")
    As.geometry('400x300')
    As['bg'] = '#5ea0c0'
    def chk():
        pdd = password.get()
        psd = passwordd.get()
        Label(root, text=f'Your Username is: {pdd} \n', pady=20, bg='#5ea0c0', fg='black', font=20).pack()

    passwordLabel = Label(As, text="Password", bg='#5ea0c0', fg='#b00d4c', font='20').pack()
    password = StringVar()
    passwordEntry = Entry(As, textvariable=password, show="*", width='30').pack()

    Button(root, text="widrowl", bg='black', fg='white', font='20', padx=10, pady=5, command=chk()).pack()
    As.mainloop()

def tr():
    psd = passwordd.get()
    Label(root, text=f'Your Username is: {psd} \n', pady=20, bg='#5ea0c0', fg='black', font=20).pack()
    Button(root, text="widrowl", bg='black', fg='white', font='20', padx=10, pady=5, command=mach()).pack()




passworddLabel = Label(root, text="Passwordd", bg='#5ea0c0', fg='#b00d4c', font='20').pack()
passwordd = StringVar()
passworddEntry = Entry(root, textvariable=passwordd, show="*", width='30').pack()

Button(root, text="widrowl", bg='black', fg='white', font='20', padx=10, pady=5, command=mach()).pack()


root.mainloop()
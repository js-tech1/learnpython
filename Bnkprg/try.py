from tkinter import *
root = Tk()
root.title("PythonGuides")
root.geometry('400x300')
root['bg'] = '#5ea0c0'

def tr():
        psd = passwordd.get()
        pwd = password.get()
        Label(root, text=f'Your Username is: {psd},{pwd} \n', pady=20, bg='#5ea0c0', fg='black', font=20).pack()

        if psd == pwd:
            Label(root, text=f'Password match', pady=20, bg='#5ea0c0', fg='black').pack()
        else:
            Label(root, text=f'Password not match', pady=20, bg='#5ea0c0', fg='black').pack()

passworddLabel = Label(root, text="Passwordd", bg='#5ea0c0', fg='#b00d4c', font='20').pack()
passwordd = StringVar()
passworddEntry = Entry(root, textvariable=passwordd, show="*", width='30').pack()

Button(root, text="widrowl", bg='black', fg='white', font='20', padx=10, pady=5, command=tr).pack()

root.mainloop()
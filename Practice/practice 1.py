from tkinter import * 



PRCT = Tk()
PRCT.title("Practice")
PRCT.geometry('400x400')
PRCT['bg'] = '#58513b'



def clear_text():
        firstnameEntry.delete(0, END)
def jack():
    pname = username.get()
    fsn = firstname.get()
    lsr = lastname.get()
    pcd = pincode.get()
    pwd = password.get()
    rpd = reenterpassword.get()

    if (pwd == rpd):
        Label(PRCT, text=f"Your Username is:{pname}\n Your Name is: {fsn} {lsr} \n{pcd} \n{pwd} \n{rpd}", pady= 10, bg='black',fg='white', font=20).place(x=740,y=470)

    else:
            Label(PRCT,text=f"Password does not match", pady=10,bg='black',fg='white').pack()
            clear_text()



firstnameLabel = Label(PRCT, text = "First Name",font=25, bg='black', fg='white',height=2). pack()
firstname = StringVar()
firstnameEntry = Entry(PRCT, textvariable=firstname, width='40').pack()


lastnameLabel = Label(PRCT,text = "Last Name",font=25, bg='black', fg='white',height=2). pack()
lastname = StringVar()
lastnameEntry = Entry(PRCT, textvariable=lastname, width='40').pack()


pincodeLabel = Label(PRCT, text="Pin Code",font=25, bg='black', fg='white',height=2).pack()
pincode = StringVar()
pincodeEntry = Entry(PRCT, textvariable=pincode,width='40').pack()


usernameLabel = Label(PRCT, text="User Name",font=25, bg='black', fg='white',height=2).pack()
username = StringVar()
usernameEntry = Entry(PRCT, textvariable=username,width='40').pack()


passwordLabel = Label(PRCT, text="Password",font=25, bg='black', fg='white',height=2).pack()
password = StringVar()
passwordEntry = Entry(PRCT, textvariable=password, show="*",width='40').pack()

reenterpasswordLabel = Label(PRCT, text="Re-enter Password",font=25, bg='black', fg='white',height=2).pack() 
reenterpassword = StringVar()
reenterpasswordEntry = Entry(PRCT, textvariable=reenterpassword, show="*",width='40').pack()


Button(PRCT,text="Register",bg='black',fg='white',font='20', padx=10, pady=5,command=jack).place(x=715,y=470)
Button.command=clear_text




PRCT.mainloop()
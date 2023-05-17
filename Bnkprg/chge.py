import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 35)
class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
    
        container = tk.Frame(self)
        container.pack()

        self.frames = {}
        for F in (Page1,Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack()
        self.show_frame()
    def show_frame(self, cont): 
        frame = self.frames[cont]
        frame.tkraise()


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Start page")

        label.pack()

        button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))
		
        button1.pack()
        button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))
        button2.pack()

class Page2(tk.Frame):
    def __init__(self, parent, controller):
    	tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Account Detailes", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
        label = ttk.Label(self, text ="Start page")

        label.pack()

        button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page2))
		
        button1.pack()

        


# class Page2(tk.Frame):

#     def __init__(self, parent, controller):
#     	tk.Frame.__init__(self, parent) 
#         label = ttk.Label(self, text ="Create Acount")
        
#         label.pack()

#         button1 = ttk.Button(self, text ="Start Page",
#         command = lambda : controller.show_frame(Page1))
	
#         button2 = ttk.Button(self, text ="Create Account",
# 							command = lambda : controller.show_frame(Page2))
#         button2.pack()

App = tkinterApp()
App.mainloop()

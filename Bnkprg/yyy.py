from msilib.schema import Class
import tkinter as tk
from tkinter import Tk, ttk



class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)

        self.frames = {}


        for F in (Start_Page, Create_Account_Page, Withdrawal_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

            self.show_frame(Start_Page)

    def show_frame(self, cont):
    	frame = self.frames[cont]
        frame.tkraise()


class Start_Page(tk.Frame):
    	def __init__(self, parent, controller):
		    tk.Frame.__init__(self, parent)
		
		
            label = ttk.Label(self, text ="Start_page", font = "20")
            
        
            label.grid(row = 0, column = 4, padx = 10, pady = 10)

            button1 = ttk.Button(self, text ="Create_Account_Page",
            command = lambda : controller.show_frame(Create_Account_Page))
        
        
            button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        
            button2 = ttk.Button(self, text ="Withdrawal_Page",
            command = lambda : controller.show_frame(Withdrawal_Page))
        
            
            button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Create_Account_Page(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Create_Account_Page", font = "20")
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

	
		button1 = ttk.Button(self, text ="Start_Page",
							command = lambda : controller.show_frame(Start_Page))
	
		
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

	
		button2 = ttk.Button(self, text ="Withdrawal_Page",
							command = lambda : controller.show_frame(Withdrawal_Page))
	
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Withdrawal_Page(tk.Frame):
    	def __init__(self, parent, controller):
		    tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Withdrawal_Page", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

	
	    button1 = ttk.Button(self, text ="Start_Page",
							command = lambda : controller.show_frame(Start_Page))
	

		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		
		button2 = ttk.Button(self, text ="Create_Account_Page",
							command = lambda : controller.show_frame(Create_Account_Pag))
	

		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


tk = tkinterApp()
Tk.mainloop()

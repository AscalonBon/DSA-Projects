from tkinter import *
from tkinter import ttk
import time

class mainProgram:
    def __init__(self, window):
        self.window = window
        self.window.title("Laboratory Exercise #3")
        self.window.geometry("800x600") #window size
        self.window.minsize(800, 600)
        self.window.maxsize(800, 600) #limits window size

        self.label = Label(window, text="Enter a string!", font=("Arial", 16), fg="#5a5a5a")
        self.label.pack(pady=16)
        
        self.input = Entry(window, width=50)
        self.input.pack(pady=10)

        self.modes = ["String Compare", "String Copy", "String Concatenation", 
                      "Palindrome", "Initials Capitalizer"]
        self.selected_mode = StringVar()
        self.selected_mode.set(self.mode[0])
        self.menu = OptionMenu(window, self.selected_mode, *self.modes)
        self.menu.pack(pady=10)
    

    


        




#main loop
window = Tk()
program = mainProgram(window)
window.mainloop()
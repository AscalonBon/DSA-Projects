from tkinter import *
from tkinter import ttk

class mainProgram:
    def __init__(self, window):
        self.window = window
        self.window.title("Laboratory Exercise #3")
        self.window.geometry("800x600")
        self.window.minsize(800, 600)
        self.window.maxsize(800, 600)

        self.label = Label(window, text="Enter a string!", font=("Arial", 16), fg="#5a5a5a")
        self.label.pack(pady=16)

        self.input1 = Entry(window, width=50)
        self.input1.pack(pady=10)
        self.input2 = Entry(window, width=50)
        self.input2.pack(pady=10)

        self.modes = ["String Copy", "String Compare", "String Concatenation", "String Length", "String Reverser"]
        self.selected_mode = StringVar()
        self.selected_mode.set(self.modes[0])
        self.menu = OptionMenu(window, self.selected_mode, *self.modes, command=self.update_input_fields)
        self.menu.pack(pady=10)

        self.execute_button = Button(window, text="Execute", command=self.execute)
        self.execute_button.pack(pady=10)

        self.result_label = Label(window, text="", font=("Arial", 14), fg="#5a5a5a")
        self.result_label.pack(pady=10)

        self.label2 = Label(window, text="2nd Input box is for string comparison, compare and concatenation!", font=("Arial", 16), fg="#5a5a5a")
        self.label2.pack(pady=16)

    def update_input_fields(self, *args):
        operation = self.selected_mode.get()
        if operation in ["String Length", "String Reverser"]:
            self.input2.pack_forget()  
        else:
            self.input2.pack(pady=10, before=self.menu)  

    def user_strcmp(self, str1, str2):
        if str1 == str2:
            return 0
        elif str1 < str2:
            return -1
        else:
            return 1

    def user_strcpy(self, str1):
        return str1[:]

    def user_strcat(self, str1, str2):
        return str1 + " " + str2

    def user_strlen(self, str1):
        return len(str1)

    def user_strrev(self, str1):
        str1 = list(str1)
        left = 0
        right = len(str1) - 1

        while left < right:
            str1[left], str1[right] = str1[right], str1[left]
            left += 1
            right -= 1
        return ''.join(str1)
    
    def execute(self):
        operation = self.selected_mode.get()
        user_input1 = self.input1.get()
        user_input2 = self.input2.get() if self.input2.winfo_ismapped() else ""

        if operation == "String Compare":
            result = self.user_strcmp(user_input1, user_input2)
            self.result_label.config(text=f"Comparison result: {result}")

        elif operation == "String Copy":
            result = self.user_strcpy(user_input1)
            self.result_label.config(text=f"New string value for str1: {result}")

        elif operation == "String Concatenation":
            result = self.user_strcat(user_input1, user_input2)
            self.result_label.config(text=f"Concatenated string: {result}")

        elif operation == "String Length":
            result = self.user_strlen(user_input1)
            self.result_label.config(text=f"'{user_input1}' The length of your string is:{result}")

        elif operation == "String Reverser":
            result = self.user_strrev(user_input1)
            self.result_label.config(text=f"Input processed: {result}")

# main loop
window = Tk()
program = mainProgram(window)
window.mainloop()

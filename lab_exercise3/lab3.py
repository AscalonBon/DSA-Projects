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

        self.modes = ["String Compare", "String Copy", "String Concatenation", "Palindrome", "Initials Capitalizer"]
        self.selected_mode = StringVar()
        self.selected_mode.set(self.modes[0])
        self.menu = OptionMenu(window, self.selected_mode, *self.modes, command=self.update_input_fields)
        self.menu.pack(pady=10)

        self.execute_button = Button(window, text="Execute", command=self.execute)
        self.execute_button.pack(pady=10)

        self.result_label = Label(window, text="", font=("Arial", 14), fg="#5a5a5a")
        self.result_label.pack(pady=10)

    def update_input_fields(self, *args):
        operation = self.selected_mode.get()
        if operation in ["Palindrome", "Initials Capitalizer"]:
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

    def is_palindrome(self, s):
        s = s.rstrip()
        return s == s[::-1]

    def capitalize_initials(self, s):
        return ' '.join(word.capitalize() for word in s.split())

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

        elif operation == "Palindrome":
            result = "is a palindrome" if self.is_palindrome(user_input1) else "is not a palindrome"
            self.result_label.config(text=f"'{user_input1}' {result}")

        elif operation == "Initials Capitalizer":
            result = self.capitalize_initials(user_input1)
            self.result_label.config(text=f"Input processed: {result}")

# main loop
window = Tk()
program = mainProgram(window)
window.mainloop()

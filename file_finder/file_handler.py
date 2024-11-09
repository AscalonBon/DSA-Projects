from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import re

class mainProgram:
    def __init__(self, window):
        self.window = window
        self.bg = "#2c2c2c"
        self.fg = "white"
        self.window.title("File Handler in Python")
        self.window.geometry("800x480")
        self.window.minsize(800, 480)
        self.window.maxsize(800, 480)
        self.window.configure(bg=self.bg)

        self.label = Label(window, text="FILE HANDLER", font=("Arial", 24), bg=self.bg, fg=self.fg)
        self.label.pack(pady=20)

        self.search_label = Label(window, text="Enter search pattern or keyword:", bg=self.bg, fg=self.fg)
        self.search_label.pack(padx=10)
        self.search_input = Entry(window, width=50)
        self.search_input.pack(pady=5)

        self.select_file_button = Button(window, text="Select File for String Search", command=self.selectFile)
        self.select_file_button.pack(pady=5)

        self.str_search_button = Button(window, text="Search String in Selected File", command=self.strFinder)
        self.str_search_button.pack(pady=5)

        self.dir_label = Label(window, text="Enter a directory (will default to This PC):", bg=self.bg, fg=self.fg)
        self.dir_label.pack(padx=10)
        self.dir_entry = Entry(window, width=50)
        self.dir_entry.pack(pady=5)

        self.file_search_button = Button(window, text="Search Files in Directory", command=self.fileFinder)
        self.file_search_button.pack(pady=5)

        self.result_frame = Frame(window)
        self.result_frame.pack(pady=10, fill=BOTH, expand=True)

        self.result_label = Label(self.result_frame, text="", font=("Arial", 12), bg=self.bg, fg=self.fg)
        self.result_label.pack(pady=10)

        self.selected_file_path = None

    def selectFile(self):
        self.selected_file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if self.selected_file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.selected_file_path}")

    def strFinder(self):
        pattern = self.search_input.get()

        if not self.selected_file_path:
            messagebox.showwarning("No File Selected", "Please select a file first.")
            return

        # Escape special characters in the pattern
        pattern = re.escape(pattern)

        try:
            with open(self.selected_file_path, 'r') as file:
                content = file.read()
                matches = re.findall(pattern, content)
                count = len(matches)
                result_text = f"The pattern '{pattern}' was found {count} times in the file."
        except FileNotFoundError:
            result_text = "File not found. Please ensure the file path is correct."
        except Exception as e:
            result_text = f"An error occurred: {str(e)}"

        self.result_label.config(text=result_text)

    def fileFinder(self):
        directories = []
        user_input_dir = self.dir_entry.get()

        if user_input_dir:
            directories.append(user_input_dir)
        else:
            home_dir = os.path.expanduser("~")
            directories = [
                os.path.join(home_dir, "Desktop"),
                os.path.join(home_dir, "Documents"),
                os.path.join(home_dir, "Downloads"),
                os.path.join(home_dir, "Music"),
                os.path.join(home_dir, "Pictures"),
                os.path.join(home_dir, "Videos")
            ]

        keyword = self.search_input.get()
        # Escape special characters in the keyword
        keyword = re.escape(keyword)
        
        found_files = []

        for directory in directories:
            if os.path.isdir(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if re.search(keyword, file, re.IGNORECASE):
                            found_files.append(os.path.join(root, file))

        result_text = ""
        if found_files:
            result_text = f"Found {len(found_files)} file(s) matching '{keyword}':\n" + "\n".join(found_files)
        else:
            result_text = f"No files found with '{keyword}' in the name."

        self.displayResults(result_text)

    def displayResults(self, result_text):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        canvas = Canvas(self.result_frame, bg=self.bg)
        scrollbar = Scrollbar(self.result_frame, orient="vertical", command=canvas.yview)

        result_text_widget = Text(canvas, wrap=WORD, width=80, height=20, font=("Arial", 12))
        result_text_widget.insert(END, result_text)
        result_text_widget.config(state=DISABLED)

        canvas.create_window((0, 0), window=result_text_widget, anchor="nw")
        canvas.config(yscrollcommand=scrollbar.set)

        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.result_frame.grid_rowconfigure(0, weight=1)
        self.result_frame.grid_columnconfigure(0, weight=1)

        canvas.config(scrollregion=canvas.bbox("all"))

window = Tk()
program = mainProgram(window)
window.mainloop()

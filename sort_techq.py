from tkinter import *
from tkinter import ttk
import time

class SortingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Sorting Techniques")
        self.window.geometry("600x400")

    
        self.label = Label(window, text="Enter 5 numbers separated by commas", font=("Arial", 14))
        self.label.pack(pady=10)

        # input field
        self.input = Entry(window, width=50)
        self.input.pack(pady=10)

        # sort button
        self.sort_button = Button(window, text="Sort", command=self.start_sorting)
        self.sort_button.pack(pady=10)

        # selecter
        self.algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Merge Sort"]
        self.selected_algorithm = StringVar()
        self.selected_algorithm.set(self.algorithms[0])
        self.algo_menu = OptionMenu(window, self.selected_algorithm, *self.algorithms)
        self.algo_menu.pack(pady=10)

        # table visuals
        self.tree = ttk.Treeview(window, columns=('Step', 'Array'), show='headings')
        self.tree.heading('Step', text='Step')
        self.tree.heading('Array', text='Result')
        self.tree.pack(pady=10, fill=BOTH, expand=True)

    def start_sorting(self):
        # prev. step visuals
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        # input and parsing
        input_data = self.input.get()
        try:
            arr = [float(x.strip()) for x in input_data.split(',')]
            if len(arr) != 5:
                raise ValueError("Please enter exactly 5 numbers.")
            
           
            selected_algo = self.selected_algorithm.get()
            self.sort_and_display(arr, selected_algo)
        except ValueError as e:
            self.tree.insert("", "end", values=(f"Error: {e}", ""))

    def update_output(self, arr, step, algorithm_name):
        # table view
        self.tree.insert("", "end", values=(step, str(arr)))
        self.window.update()
        time.sleep(1)  # delay for visuals

    # sorting techniques
    def bubble_sort(self, arr):
        arr = arr.copy()
        n = len(arr)
        step = 1
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                self.update_output(arr, step, "Bubble Sort")
                step += 1

    def insertion_sort(self, arr):
        arr = arr.copy()
        step = 1
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                self.update_output(arr, step, "Insertion Sort")
                step += 1
            arr[j + 1] = key
            self.update_output(arr, step, "Insertion Sort")
            step += 1

    def selection_sort(self, arr):
        arr = arr.copy()
        step = 1
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.update_output(arr, step, "Selection Sort")
            step += 1

    def quick_sort(self, arr, low, high, step=1):
        if low < high:
            pi = self.partition(arr, low, high)
            self.update_output(arr, step, "Quick Sort")
            step += 1
            step = self.quick_sort(arr, low, pi - 1, step)
            step = self.quick_sort(arr, pi + 1, high, step)
        return step

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def merge_sort(self, arr, step=1):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            step = self.merge_sort(L, step)
            step = self.merge_sort(R, step)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                self.update_output(arr, step, "Merge Sort")
                step += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                self.update_output(arr, step, "Merge Sort")
                step += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                self.update_output(arr, step, "Merge Sort")
                step += 1
        return step

    # display
    def sort_and_display(self, arr, algorithm_name):
        if algorithm_name == "Bubble Sort":
            self.bubble_sort(arr)
        elif algorithm_name == "Insertion Sort":
            self.insertion_sort(arr)
        elif algorithm_name == "Selection Sort":
            self.selection_sort(arr)
        elif algorithm_name == "Quick Sort":
            self.quick_sort(arr.copy(), 0, len(arr) - 1)
        elif algorithm_name == "Merge Sort":
            self.merge_sort(arr.copy())


# Main application
window = Tk()
app = SortingApp(window)
window.mainloop()

import tkinter as tk
from tkinter import messagebox  # Import messagebox
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Sorting Visualizer")
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.array = []
        self.rects = []

        # Frame for user input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        # Entry for input array
        self.entry = tk.Entry(self.input_frame, width=50)
        self.entry.pack(side=tk.LEFT)

        # Button to update array
        update_button = tk.Button(self.input_frame, text="Update Array", command=self.update_array)
        update_button.pack(side=tk.LEFT)

        # Buttons to choose sorting algorithms
        bubble_sort_button = tk.Button(self.root, text="Bubble Sort", command=self.start_bubble_sort)
        bubble_sort_button.pack(side=tk.LEFT)

        selection_sort_button = tk.Button(self.root, text="Selection Sort", command=self.start_selection_sort)
        selection_sort_button.pack(side=tk.LEFT)

        insertion_sort_button = tk.Button(self.root, text="Insertion Sort", command=self.start_insertion_sort)
        insertion_sort_button.pack(side=tk.LEFT)

    def update_array(self):
        input_data = self.entry.get()
        try:
            # Handle spaces and strip them before splitting into integers
            self.array = list(map(int, input_data.replace(" ", "").split(',')))  
            self.draw_array()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter comma-separated integers.")

    def draw_array(self):
        self.canvas.delete("all")
        width = 600 // len(self.array)  # Dynamic width based on array size
        for i, value in enumerate(self.array):
            # Draw rectangles representing the array elements
            self.canvas.create_rectangle(i * width, 400 - value, (i + 1) * width, 400, fill="blue")
            # Display the value of each array element above its rectangle
            self.canvas.create_text(i * width + width // 2, 400 - value - 10, text=str(value), fill="white")

    def start_bubble_sort(self):
        self.bubble_sort()

    def start_selection_sort(self):
        self.selection_sort()

    def start_insertion_sort(self):
        self.insertion_sort()

    # Sorting Algorithms with Visualization

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array()
                    self.root.update()
                    time.sleep(0.2)  # Add delay for visualization

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array()
            self.root.update()
            time.sleep(0.2)  # Add delay for visualization

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_array()
            self.root.update()
            time.sleep(0.2)  # Add delay for visualization


# Main window setup to run the visualizer
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = SortingVisualizer(root)
    root.mainloop()

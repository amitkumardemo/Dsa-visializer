import tkinter as tk
import time

class SearchingVisualizer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Searching Visualizer")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Sample array for searching
        self.array = []
        self.rects = []
        self.target = 9  # Value to search for

        # Input box for array
        self.input_box = tk.Entry(self.root)
        self.input_box.pack()

        # Buttons for Searching Methods
        linear_button = tk.Button(self.root, text="Start Linear Search", command=self.linear_search)
        linear_button.pack(side=tk.LEFT)

        binary_button = tk.Button(self.root, text="Start Binary Search", command=self.binary_search)
        binary_button.pack(side=tk.LEFT)

        # Label for messages
        self.message_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.message_label.pack()

        # Button to create array from input
        create_array_button = tk.Button(self.root, text="Create Array", command=self.create_array)
        create_array_button.pack()

        self.draw_array()

    def create_array(self):
        input_data = self.input_box.get()
        try:
            self.array = list(map(int, input_data.split(',')))  # Create array from input
            self.draw_array()  # Redraw the array
            self.message_label.config(text="Array Created!")  # Message for array creation
            self.message_label.config(bg="lightgreen")  # Change color of message
        except ValueError:
            self.message_label.config(text="Invalid Input! Please enter integers separated by commas.")
            self.message_label.config(bg="red")

    def draw_array(self):
        self.canvas.delete("all")  # Clear previous drawings
        self.rects = []  # Reset rectangles
        width = 50
        for i, value in enumerate(self.array):
            rect = self.canvas.create_rectangle(i * width, 150, (i + 1) * width, 200, fill="blue")
            text = self.canvas.create_text(i * width + 25, 175, text=str(value), fill="white")
            self.rects.append((rect, text))

    def linear_search(self):
        self.message_label.config(text="Linear Search Started")  # Message for Linear Search
        self.message_label.config(bg="lightblue")  # Change color of message
        searches = 0  # Initialize search count
        for i, value in enumerate(self.array):
            self.canvas.itemconfig(self.rects[i][0], fill="red")  # Highlight the current element
            self.root.update()
            time.sleep(0.5)  # Pause for effect
            searches += 1  # Increment search count
            
            if value == self.target:
                self.canvas.itemconfig(self.rects[i][0], fill="red")  # Change to red if found
                self.message_label.config(text=f"Linear Search: Found! Searches: {searches}")  # Update message
                self.message_label.config(bg="lightgreen")  # Change color of message
                break
            self.canvas.itemconfig(self.rects[i][0], fill="blue")  # Reset color
            self.root.update()
        else:
            self.message_label.config(text="Linear Search: Not Found!")  # Not found message

    def binary_search(self):
        self.message_label.config(text="Binary Search Started")  # Message for Binary Search
        self.message_label.config(bg="lightblue")  # Change color of message
        searches = 0  # Initialize search count
        left, right = 0, len(self.array) - 1
        
        while left <= right:
            mid = (left + right) // 2
            self.canvas.itemconfig(self.rects[mid][0], fill="red")  # Highlight the middle element
            self.root.update()
            time.sleep(0.5)  # Pause for effect
            
            searches += 1  # Increment search count
            
            if self.array[mid] == self.target:
                self.canvas.itemconfig(self.rects[mid][0], fill="yellow")  # Change to yellow if found
                self.message_label.config(text=f"Binary Search: Found! Searches: {searches}")  # Update message
                self.message_label.config(bg="lightgreen")  # Change color of message
                break
            elif self.array[mid] < self.target:
                left = mid + 1  # Move the left index
            else:
                right = mid - 1  # Move the right index

            # Reset colors
            for i in range(len(self.array)):
                if i != mid:
                    self.canvas.itemconfig(self.rects[i][0], fill="blue")
            self.root.update()
        else:
            self.message_label.config(text="Binary Search: Not Found!")  # Not found message


# Main application to run the visualizer
if __name__ == "__main__":
    root = tk.Tk()
    app = SearchingVisualizer(root)
    root.mainloop()

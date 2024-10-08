import tkinter as tk
from tkinter import messagebox

class QueueVisualizer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Queue Visualizer")
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.queue = []
        self.rects = []

        # Frame for input and buttons
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        # Entry for enqueuing values
        self.entry = tk.Entry(self.input_frame, width=10)
        self.entry.pack(side=tk.LEFT)

        # Buttons for Queue Operations
        enqueue_button = tk.Button(self.input_frame, text="Enqueue", command=self.enqueue)
        enqueue_button.pack(side=tk.LEFT)

        dequeue_button = tk.Button(self.input_frame, text="Dequeue", command=self.dequeue)
        dequeue_button.pack(side=tk.LEFT)

        peek_button = tk.Button(self.input_frame, text="Front", command=self.peek)
        peek_button.pack(side=tk.LEFT)

        is_empty_button = tk.Button(self.input_frame, text="Is Empty", command=self.is_empty)
        is_empty_button.pack(side=tk.LEFT)

    def enqueue(self):
        try:
            value = self.entry.get()
            if not value:
                raise ValueError("Please enter a value to enqueue.")
            
            self.queue.append(value)
            self.entry.delete(0, tk.END)

            # Create a rectangle and a text to represent the queue element
            rect = self.canvas.create_rectangle(50 + len(self.queue)*40, 150, 90 + len(self.queue)*40, 190, fill="green")
            text = self.canvas.create_text(70 + len(self.queue)*40, 170, text=str(value), fill="white")
            self.rects.append((rect, text))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
            rect, text = self.rects.pop(0)
            self.canvas.delete(rect)
            self.canvas.delete(text)

            # Move the remaining elements to the left
            for i in range(len(self.rects)):
                self.canvas.move(self.rects[i][0], -40, 0)
                self.canvas.move(self.rects[i][1], -40, 0)
        else:
            messagebox.showwarning("Warning", "The queue is empty, nothing to dequeue.")

    def peek(self):
        if self.queue:
            front_value = self.queue[0]
            messagebox.showinfo("Front of Queue", f"Front element: {front_value}")
        else:
            messagebox.showwarning("Warning", "The queue is empty, no front element.")

    def is_empty(self):
        if not self.queue:
            messagebox.showinfo("Queue Status", "The queue is empty.")
        else:
            messagebox.showinfo("Queue Status", "The queue is not empty.")

# Main window setup to run the visualizer
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = QueueVisualizer(root)
    root.mainloop()

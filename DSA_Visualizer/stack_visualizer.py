import tkinter as tk
from tkinter import messagebox

class StackVisualizer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Stack Visualizer")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.stack = []
        self.rects = []

        # Frame for the entry and buttons
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        # Entry to take input for pushing onto the stack
        self.entry = tk.Entry(self.input_frame, width=10)
        self.entry.pack(side=tk.LEFT)

        # Buttons for Stack Operations
        push_button = tk.Button(self.input_frame, text="Push", command=self.push)
        push_button.pack(side=tk.LEFT)

        pop_button = tk.Button(self.input_frame, text="Pop", command=self.pop)
        pop_button.pack(side=tk.LEFT)

        peek_button = tk.Button(self.input_frame, text="Peek", command=self.peek)
        peek_button.pack(side=tk.LEFT)

        is_empty_button = tk.Button(self.input_frame, text="Is Empty", command=self.is_empty)
        is_empty_button.pack(side=tk.LEFT)

    def push(self):
        try:
            value = self.entry.get()
            if not value:  # If entry is empty, show a message
                raise ValueError("Please enter a value to push.")
            self.stack.append(value)
            self.entry.delete(0, tk.END)
            
            # Create a rectangle and a text inside it representing the stack element
            rect = self.canvas.create_rectangle(150, 350 - len(self.stack) * 40, 250, 400 - len(self.stack) * 40, fill="blue")
            text = self.canvas.create_text(200, 375 - len(self.stack) * 40, text=str(value), fill="white")
            self.rects.append((rect, text))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def pop(self):
        if self.stack:
            self.stack.pop()
            rect, text = self.rects.pop()
            self.canvas.delete(rect)
            self.canvas.delete(text)
        else:
            messagebox.showwarning("Warning", "The stack is empty, nothing to pop.")

    def peek(self):
        if self.stack:
            top_value = self.stack[-1]
            messagebox.showinfo("Top of Stack", f"Top element: {top_value}")
        else:
            messagebox.showwarning("Warning", "The stack is empty, no top element.")

    def is_empty(self):
        if not self.stack:
            messagebox.showinfo("Stack Status", "The stack is empty.")
        else:
            messagebox.showinfo("Stack Status", "The stack is not empty.")

# Main window setup to run the visualizer
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = StackVisualizer(root)
    root.mainloop()

import tkinter as tk

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self._insert(current_node.left, value)
            else:
                current_node.left = Node(value)
        else:
            if current_node.right:
                self._insert(current_node.right, value)
            else:
                current_node.right = Node(value)

class TreeVisualizer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Tree Visualizer")
        self.canvas = tk.Canvas(self.root, width=600, height=500)
        self.canvas.pack()

        self.tree = BinaryTree()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.entry = tk.Entry(self.input_frame)
        self.entry.pack(side=tk.LEFT)
        insert_button = tk.Button(self.input_frame, text="Insert", command=self.insert_node)
        insert_button.pack(side=tk.LEFT)

        self.visualize_tree()

    def insert_node(self):
        value = int(self.entry.get())
        self.tree.insert(value)
        self.entry.delete(0, tk.END)
        self.visualize_tree()

    def visualize_tree(self):
        self.canvas.delete("all")
        if self.tree.root:
            self._draw_tree(self.tree.root, 300, 50, 150)

    def _draw_tree(self, node, x, y, offset):
        if node.left:
            self.canvas.create_line(x, y, x - offset, y + 70)
            self._draw_tree(node.left, x - offset, y + 70, offset // 2)
        if node.right:
            self.canvas.create_line(x, y, x + offset, y + 70)
            self._draw_tree(node.right, x + offset, y + 70, offset // 2)

        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="blue")
        self.canvas.create_text(x, y, text=str(node.value), fill="white")

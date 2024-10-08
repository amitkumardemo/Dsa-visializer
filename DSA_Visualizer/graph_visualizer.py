import tkinter as tk
from tkinter import simpledialog, messagebox

class GraphVisualizer:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Graph Visualizer")
        self.canvas = tk.Canvas(self.root, width=600, height=500)
        self.canvas.pack()

        self.graph = {}  # Adjacency list to store graph
        self.nodes = {}
        self.node_radius = 20
        self.edges = {}  # Store edges and weights

        # Create buttons for adding nodes, edges, and clearing the canvas
        self.add_node_button = tk.Button(self.root, text="Add Node", command=self.add_node)
        self.add_node_button.pack(side=tk.LEFT)

        self.add_edge_button = tk.Button(self.root, text="Add Edge", command=self.add_edge)
        self.add_edge_button.pack(side=tk.LEFT)

        self.delete_node_button = tk.Button(self.root, text="Delete Node", command=self.delete_node)
        self.delete_node_button.pack(side=tk.LEFT)

        self.delete_edge_button = tk.Button(self.root, text="Delete Edge", command=self.delete_edge)
        self.delete_edge_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.root, text="Clear Graph", command=self.clear_graph)
        self.clear_button.pack(side=tk.LEFT)

        # Text box for user input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side=tk.BOTTOM)

        self.node_input_label = tk.Label(self.input_frame, text="Node (x,y): ")
        self.node_input_label.pack(side=tk.LEFT)
        self.node_input_entry = tk.Entry(self.input_frame, width=15)
        self.node_input_entry.pack(side=tk.LEFT)

        self.weight_input_label = tk.Label(self.input_frame, text="Weight (start,end): ")
        self.weight_input_label.pack(side=tk.LEFT)
        self.weight_input_entry = tk.Entry(self.input_frame, width=15)
        self.weight_input_entry.pack(side=tk.LEFT)

        self.add_from_input_button = tk.Button(self.input_frame, text="Add from Input", command=self.add_from_input)
        self.add_from_input_button.pack(side=tk.LEFT)

        self.current_node_id = 0
        self.start_node = None

    def add_node(self):
        self.canvas.bind("<Button-1>", self.create_node)

    def create_node(self, event):
        node_id = self.current_node_id
        self.graph[node_id] = []
        x, y = event.x, event.y
        self.nodes[node_id] = (x, y)
        self.current_node_id += 1

        # Draw the node on the canvas
        self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius, fill="blue")
        self.canvas.create_text(x, y, text=str(node_id), fill="white")
        
        self.canvas.unbind("<Button-1>")

    def add_edge(self):
        self.canvas.bind("<Button-1>", self.select_start_node)

    def select_start_node(self, event):
        for node_id, (x, y) in self.nodes.items():
            if abs(x - event.x) < self.node_radius and abs(y - event.y) < self.node_radius:
                self.start_node = node_id
                self.canvas.bind("<Button-1>", self.select_end_node)
                break

    def select_end_node(self, event):
        for node_id, (x, y) in self.nodes.items():
            if abs(x - event.x) < self.node_radius and abs(y - event.y) < self.node_radius:
                end_node = node_id
                if end_node != self.start_node:  # Avoid self-loop
                    self.graph[self.start_node].append(end_node)
                    self.graph[end_node].append(self.start_node)

                    # Get edge weight from user
                    weight = simpledialog.askinteger("Edge Weight", "Enter weight for the edge:", minvalue=1)
                    if weight is not None:
                        self.edges[(self.start_node, end_node)] = weight
                        self.edges[(end_node, self.start_node)] = weight

                    x1, y1 = self.nodes[self.start_node]
                    x2, y2 = self.nodes[end_node]
                    line = self.canvas.create_line(x1, y1, x2, y2)
                    # Display the weight of the edge
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    self.canvas.create_text(mid_x, mid_y, text=str(weight), fill="black")
                break
        self.canvas.unbind("<Button-1>")

    def add_from_input(self):
        node_input = self.node_input_entry.get()
        if node_input:
            try:
                x, y = map(int, node_input.split(','))
                self.create_node_from_input(x, y)
                self.node_input_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Input Error", "Invalid input. Use format: x,y")
        
        edge_input = self.weight_input_entry.get()
        if edge_input:
            try:
                start, end = map(int, edge_input.split(','))
                if start in self.nodes and end in self.nodes:
                    weight = simpledialog.askinteger("Edge Weight", "Enter weight for the edge:", minvalue=1)
                    if weight is not None:
                        self.add_edge_from_input(start, end, weight)
                        self.weight_input_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Input Error", "Both nodes must exist.")
            except ValueError:
                messagebox.showerror("Input Error", "Invalid input. Use format: start,end")

    def create_node_from_input(self, x, y):
        node_id = self.current_node_id
        self.graph[node_id] = []
        self.nodes[node_id] = (x, y)
        self.current_node_id += 1

        # Draw the node on the canvas
        self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius, fill="blue")
        self.canvas.create_text(x, y, text=str(node_id), fill="white")

    def add_edge_from_input(self, start, end, weight):
        if start != end:
            self.graph[start].append(end)
            self.graph[end].append(start)
            self.edges[(start, end)] = weight
            self.edges[(end, start)] = weight

            # Draw the edge on the canvas
            x1, y1 = self.nodes[start]
            x2, y2 = self.nodes[end]
            line = self.canvas.create_line(x1, y1, x2, y2)
            # Display the weight of the edge
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            self.canvas.create_text(mid_x, mid_y, text=str(weight), fill="black")

    def delete_node(self):
        self.canvas.bind("<Button-1>", self.select_node_for_deletion)

    def select_node_for_deletion(self, event):
        for node_id, (x, y) in self.nodes.items():
            if abs(x - event.x) < self.node_radius and abs(y - event.y) < self.node_radius:
                # Remove the node and its edges from the graph
                for neighbor in self.graph[node_id]:
                    self.graph[neighbor].remove(node_id)
                    del self.edges[(neighbor, node_id)]
                    del self.edges[(node_id, neighbor)]
                del self.graph[node_id]
                del self.nodes[node_id]
                self.redraw_graph()
                break
        self.canvas.unbind("<Button-1>")

    def delete_edge(self):
        self.canvas.bind("<Button-1>", self.select_edge_for_deletion)

    def select_edge_for_deletion(self, event):
        for node_id, (x, y) in self.nodes.items():
            if abs(x - event.x) < self.node_radius and abs(y - event.y) < self.node_radius:
                if self.start_node is None:
                    self.start_node = node_id
                    self.canvas.bind("<Button-1>", self.select_edge_end_node)
                else:
                    end_node = node_id
                    if end_node in self.graph[self.start_node]:
                        self.graph[self.start_node].remove(end_node)
                        self.graph[end_node].remove(self.start_node)
                        del self.edges[(self.start_node, end_node)]
                        del self.edges[(end_node, self.start_node)]
                        self.redraw_graph()
                    self.start_node = None
                    self.canvas.unbind("<Button-1>")
                break

    def redraw_graph(self):
        self.canvas.delete("all")
        for node_id, (x, y) in self.nodes.items():
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius, fill="blue")
            self.canvas.create_text(x, y, text=str(node_id), fill="white")
        for (start, end), weight in self.edges.items():
            x1, y1 = self.nodes[start]
            x2, y2 = self.nodes[end]
            line = self.canvas.create_line(x1, y1, x2, y2)
            # Display the weight of the edge
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            self.canvas.create_text(mid_x, mid_y, text=str(weight), fill="black")

    def clear_graph(self):
        self.graph.clear()
        self.nodes.clear()
        self.edges.clear()
        self.canvas.delete("all")
        self.current_node_id = 0

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    app = GraphVisualizer(root)
    root.mainloop()

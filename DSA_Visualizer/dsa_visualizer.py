import tkinter as tk
from stack_visualizer import StackVisualizer
from queue_visualizer import QueueVisualizer
from sorting_visualizer import SortingVisualizer
from searching_visualizer import SearchingVisualizer
from tree_visualizer import TreeVisualizer
from graph_visualizer import GraphVisualizer

class DSAVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA Visualizer")
        self.root.geometry("800x600")
        
        # Create main menu
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        
        # Create the "Data Structures" menu
        dsa_menu = tk.Menu(menu_bar, tearoff=0)
        dsa_menu.add_command(label="Stack", command=self.open_stack)
        dsa_menu.add_command(label="Queue", command=self.open_queue)
        dsa_menu.add_command(label="Sorting", command=self.open_sorting)
        dsa_menu.add_command(label="Searching", command=self.open_searching)
        dsa_menu.add_command(label="Tree", command=self.open_tree)
        dsa_menu.add_command(label="Graph", command=self.open_graph)
        menu_bar.add_cascade(label="Menu", menu=dsa_menu)
        
        # Add the menu bar to the root window
        self.root.config(menu=menu_bar)

    # Handlers to open the respective visualizers
    def open_stack(self):
        StackVisualizer(self.root)

    def open_queue(self):
        QueueVisualizer(self.root)

    def open_sorting(self):
        SortingVisualizer(self.root)

    def open_searching(self):
        SearchingVisualizer(self.root)

    def open_tree(self):
        TreeVisualizer(self.root)

    def open_graph(self):
        GraphVisualizer(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = DSAVisualizerApp(root)
    root.mainloop()

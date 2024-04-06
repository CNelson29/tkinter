import tkinter as tk

class Frame(tk.Frame):
    def int(self, root = None):
        super().int(root,height=1000,width=640)
        self.root = root
        self.pack()
        self.config(bg='blue')
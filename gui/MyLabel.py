# Import relevant libraries
import tkinter as tk

class myLabel:
    """
    Custom label class for the GUI
    """
    def __init__(self, window, text, font, bg, fg):
        self.window = window
        self.text = text
        self.font = font        # ("Helvetica", 12, "bold")
        self.bg = bg
        self.fg = fg


    def create(self, x, y):
        """
        Create the custom label
        x: x coordinate of the label
        y: y coordinate of the label
        """
        self.mylabel =  tk.Label(self.window, text = self.text, font=self.font, bg=self.bg, fg=self.fg)
        self.mylabel.place(x=x, y=y)
        return self.mylabel

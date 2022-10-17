# Import all relevant libraries and custom defined classes 
from tkinter import *
import tkinter as tk

from MyLabel import myLabel
from Dataset_menu import Dataset_menu
from Test_acc_gender import Test_acc_gender
from Instructions import Instructions
from Model_menu import Model_menu


def start_application():
     """
     This function starts the application of the GUI 
     """
     # Create and configure window:
     window = tk.Tk()
     window.configure(background="#ffffff")  # background
     window.geometry("800x600")  # size
     window.title("Gender bias in Face Recognition GUI")  # title

     # create dropdown menu for dataset selection
     dataset_menu = Dataset_menu(window)
     dataset_menu.create(x=265, y=150)

     # create dropdown menu for model selection
     model_menu = Model_menu(window, dataset_menu)
     model_menu.create(x=265, y=190)

     # create accuracy and gender testing for (Current, previous, comparison)
     test_model = Test_acc_gender(window, dataset_menu, model_menu)
     test_model.main()

     # create instructions for buttons
     instructions = Instructions(window)
     instructions.main()

     # Start the window, Create text entry box for : status field
     statusField = tk.Entry(window)
     # window.mainloop()
     return window


if __name__ == "__main__":
     start_application().mainloop()
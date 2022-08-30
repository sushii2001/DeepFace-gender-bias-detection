from tkinter import *
import tkinter as tk

from MyLabel import myLabel
from Dataset_menu import Dataset_menu
from Test_acc_gender import Test_acc_gender
from Instructions import Instructions
from Model_menu import Model_menu


if __name__ == "__main__":
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

     # create bar plot
     # import matplotlib, numpy, sys
     # matplotlib.use('TkAgg')
     # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
     # from matplotlib.figure import Figure
     # if sys.version_info[0] < 3:
     #      import Tkinter as Tk
     # else:
     #      import tkinter as Tk

     # root = Tk.Tk()

     # f = Figure(figsize=(5,4), dpi=100)
     # ax = f.add_subplot(111)

     # data = (20, 35, 30, 35, 27)

     # ind = numpy.arange(5)  # the x locations for the groups
     # width = .5

     # rects1 = ax.bar(ind, data, width)

     # canvas = FigureCanvasTkAgg(f, master=root)
     # canvas.draw()
     # canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

     # Tk.mainloop()

     # create instructions for buttons
     instructions = Instructions(window)
     instructions.main()

     # Start the window, Create text entry box for : status field
     statusField = tk.Entry(window)
     window.mainloop()
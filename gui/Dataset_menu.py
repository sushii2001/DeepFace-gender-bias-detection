from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from MyLabel import myLabel

class Dataset_menu:
    # DATASETS
    DATASETS_OPTIONS = [
        "LFW (Male)",
        "LFW (Female)",
        "LFW (Male + Makeup)",
        "LFW (Female + Makeup)",
        "LFW (Male + Mask)",
        "LFW (Female + Mask)",
    ]
    
    CURRENT_DATASET = DATASETS_OPTIONS[0]

    def __init__(self, window):
        self.datasetValue = StringVar()  # datatype of menu text
        self.datasetValue.set(Dataset_menu.DATASETS_OPTIONS[0])  # initial menu text
        self.window = window

    def create(self, x, y):
        drop = OptionMenu(
            self.window, self.datasetValue, *(Dataset_menu.DATASETS_OPTIONS),
            command= lambda _: self.menu_check_btn(self.datasetValue)
        )
        drop.pack()
        drop.place(x=x, y=y)

        # Label for datasetLabel:
        datasetLabel = myLabel(self.window, "Dataset", "Helvetica", "#ffffff", "#000000")
        datasetLabel.create(x=165, y=150)

        # Add image:
        frame = tk.Frame(self.window)
        frame.place(x=50, y=120)
        img = ImageTk.PhotoImage(Image.open("./data/LFW/Luis_Ernesto_Derbez_Bautista/Luis_Ernesto_Derbez_Bautista_0001.jpg").resize((100, 100)))
        label = tk.Label(frame, image=img)
        label.configure(image=img)
        label.img = img
        label.pack()

    # Dropdown function:
    def menu_check_btn(self, datasetValue):
        # Add image:
        frame = tk.Frame(self.window)
        frame.place(x=50, y=120)
        img = ImageTk.PhotoImage(Image.open("./data/LFW/Luis_Ernesto_Derbez_Bautista/Luis_Ernesto_Derbez_Bautista_0001.jpg").resize((100, 100)))
        label = tk.Label(frame, image=img)
        label.pack()            

        Dataset_menu.CURRENT_DATASET = datasetValue.get()
        if Dataset_menu.CURRENT_DATASET == "LFW (Male)":
            img = ImageTk.PhotoImage(
                Image.open("./data/LFW/Luis_Ernesto_Derbez_Bautista/Luis_Ernesto_Derbez_Bautista_0001.jpg").resize((100, 100))
            )
            label.configure(image=img)
            label.img = img

        elif Dataset_menu.CURRENT_DATASET == "LFW (Female)":
            img = ImageTk.PhotoImage(
                Image.open("./data/LFW/Angelina_Jolie/Angelina_Jolie_0001.jpg").resize((100, 100))
            )
            label.configure(image=img)
            label.img = img

        elif Dataset_menu.CURRENT_DATASET == "LFW (Male + Makeup)":
            img = ImageTk.PhotoImage(
                Image.open("./data/LFW/Luis_Ernesto_Derbez_Bautista/Luis_Ernesto_Derbez_Bautista_0001.jpg").resize((100, 100))
            )
            label.configure(image=img)
            label.img = img

        elif Dataset_menu.CURRENT_DATASET == "LFW (Female + Makeup)":
            img = ImageTk.PhotoImage(
                Image.open("./data/LFW/Angelina_Jolie/Angelina_Jolie_0001.jpg").resize((100, 100))
            )
            label.configure(image=img)
            label.img = img
        elif Dataset_menu.CURRENT_DATASET == "LFW (Male + Mask)":
            img = ImageTk.PhotoImage(
                Image.open("./data/LFW/Luis_Ernesto_Derbez_Bautista/Luis_Ernesto_Derbez_Bautista_0001.jpg").resize((100, 100))
            )
            label.configure(image=img)
            label.img = img

        elif Dataset_menu.CURRENT_DATASET == "LFW (Female + Mask)":
            img = ImageTk.PhotoImage(
                Image.open("./data/LFW/Angelina_Jolie/Angelina_Jolie_0001.jpg").resize((100, 100))
            )
            label.configure(image=img)
            label.img = img
        else:
            pass
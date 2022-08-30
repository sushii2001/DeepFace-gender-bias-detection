from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from MyLabel import myLabel
import pandas as pd

class Model_menu:
    # MODELS options
    MODELS_OPTIONS = [
        "Facenet512", 
        "Facenet", 
        "VGG-Face", 
        "OpenFace", 
        "DeepFace", 
        "ArcFace"
    ]
    
    CURRENT_MODEL = MODELS_OPTIONS[0]

    def __init__(self, window, dataset_value):
        self.model_value = StringVar()  # datatype of menu text
        self.model_value.set(Model_menu.MODELS_OPTIONS[0])  # initial menu text
        self.window = window
        self.dataset_value = dataset_value
        self.results_lfw = pd.read_csv('./result/deepface_benchmark_mod.csv')

    def create(self, x, y):
        drop = OptionMenu(
            self.window, self.model_value, *(Model_menu.MODELS_OPTIONS),
            command= lambda _: self.menu_check_btn(self.model_value)
        )
        drop.pack()
        drop.place(x=x, y=y)

        # Label for model Label:
        model_label = myLabel(self.window, "Model", "Helvetica", "#ffffff", "#000000")
        model_label.create(x=165, y=190)

    # Dropdown function:
    def menu_check_btn(self, model_value):

        Model_menu.CURRENT_MODEL = model_value.get()
        # dataset_value = self.dataset_value.CURRENT_DATASET

        # ###### Current Accuracy ######
        # accuracy_label = myLabel(self.window, "Accuracy: ", "Helvetica", "#ffffff", "#000000")
        # accuracy_value = myLabel(self.window, "0.0%", "Helvetica", "#12ed96", "#000000")
        # accuracy_label.create(x=430, y=100)
        # accuracy_value = accuracy_value.create(x=525, y=100)

        # if Model_menu.CURRENT_MODEL == "Facenet512" and dataset_value == "LFW (Male)":
        #     accuracy = self.results_lfw.iloc[0,2]
        #     accuracy_value["text"] = str(accuracy) + "%"

        # elif Model_menu.CURRENT_MODEL == "Facenet" and dataset_value == "LFW (Male)":
        #     accuracy = self.results_lfw.iloc[2,2]
        #     accuracy_value["text"] = str(accuracy) + "%"
        
        # else:
        #     print("GG")
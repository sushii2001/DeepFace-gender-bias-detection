# Import relevant libraries
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
    
    # Set current model on GUI to the first model in the list
    CURRENT_MODEL = MODELS_OPTIONS[0]

    def __init__(self, window, dataset_value):
        self.model_value = StringVar()  # datatype of menu text
        self.model_value.set(Model_menu.MODELS_OPTIONS[0])  # initial menu text
        self.window = window
        self.dataset_value = dataset_value
        self.results_lfw = pd.read_csv('./result/deepface_benchmark_gender_nonperturbed.csv')

    def create(self, x, y):
        """
        Create the model menu
        x: x coordinate of the model menu
        y: y coordinate of the model menu
        """
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
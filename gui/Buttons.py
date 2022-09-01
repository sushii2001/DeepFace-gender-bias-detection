from operator import mod
import tkinter as tk
import random as rd
import pandas as pd

class Buttons:
    def __init__(self, window, value=None) -> None:
        self.window = window
        self.value = value
        self.results_fr = pd.read_csv('./result/deepface_gui_face_recognition.csv')
        self.results_gender = pd.read_csv('./result/deepface_gui_gender.csv')
        # self.results_lfw = pd.read_csv('./result/deepface_benchmark_mod.csv')
        self.results_lfw = pd.read_csv('./result/deepface_benchmark_gender.csv')

    def test_btn_sample(self, accuracy, updated_accuracy, gender, gender_value, dataset_current):
        if dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[0,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[1,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        # elif dataset_current == "LFW (Male + Makeup)":
        #     updated_accuracy = self.results.iloc[1,1]
        #     accuracy["text"] = str(updated_accuracy) + "%"

        #     GENDER_VAL = ["MALE", "FEMALE"]
        #     gender = rd.choices(GENDER_VAL)
        #     gender_value["text"] = str(gender.pop())

        # elif dataset_current == "LFW (Female + Makeup)":
        #     updated_accuracy = self.results.iloc[1,1]
        #     accuracy["text"] = str(updated_accuracy) + "%"

        #     GENDER_VAL = ["MALE", "FEMALE"]
        #     gender = rd.choices(GENDER_VAL)
        #     gender_value["text"] = str(gender.pop())
        else: 
            print(dataset_current)

    def test_btn_full(self, accuracy, updated_accuracy, gender, gender_value, dataset_current, model_current):
        if model_current == "Facenet512" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_lfw.iloc[0,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_lfw.iloc[2,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_lfw.iloc[4,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_lfw.iloc[6,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_lfw.iloc[8,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_lfw.iloc[10,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet512" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_lfw.iloc[1,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_lfw.iloc[3,2]
            accuracy["text"] = str(updated_accuracy) + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_lfw.iloc[5,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_lfw.iloc[7,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_lfw.iloc[9,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_lfw.iloc[11,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        else: 
            print(model_current)

        gender_value["text"] = ""

    def save_btn(self, accuracy_val, dataset, model, accuracy_current, dataset_value, model_name):
        accuracy_val["text"] = accuracy_current["text"]
        dataset["text"] = dataset_value
        model["text"] = model_name

    def compare_btn(self, accuracy_current, accuracy_prev, accuracy_diff):

        try: 
            def p2f(x):
                return float(x.strip('%'))

            result = round(p2f(accuracy_current["text"]) - p2f(accuracy_prev["text"]), 2)
            if result > 0:
                accuracy_diff["text"] = "+" + str(result) + "%"
                accuracy_diff["bg"] = "#12ed96"
            else:
                accuracy_diff["text"] = str(result) + "%"
                accuracy_diff["bg"] = "red"

            

        except Exception as e:
            print(e)
            print("Please Save a Model first before Compare!")




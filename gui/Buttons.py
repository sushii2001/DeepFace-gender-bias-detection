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
        self.results_lfw = pd.read_csv('./result/deepface_benchmark_gender_nonperturbed.csv')
        self.results_lfw_makeup = pd.read_csv('./result/deepface_benchmark_gender_perturbed.csv')

    def test_btn_sample(self, accuracy, updated_accuracy, gender, gender_value, dataset_current, model_current):
        if model_current == "Facenet512" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[0,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[1,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[2,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[3,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[4,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Male)":
            updated_accuracy = self.results_fr.iloc[5,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[0,1]
            gender_value["text"] = gender

        elif model_current == "Facenet512" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[6,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[7,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[8,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[9,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[10,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Female)":
            updated_accuracy = self.results_fr.iloc[11,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[1,1]
            gender_value["text"] = gender

        # Light Makeup Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[12,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[2,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[13,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[2,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[14,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[2,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[15,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[2,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[16,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[2,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[17,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[2,1]
            gender_value["text"] = gender

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[18,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[3,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[19,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[3,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[20,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[3,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[21,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[3,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[22,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[3,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_fr.iloc[23,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[3,1]
            gender_value["text"] = gender

        # Heavy Makeup Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[24,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[4,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[25,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[4,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[26,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[4,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[27,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[4,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[28,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[4,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[29,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[4,1]
            gender_value["text"] = gender

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[30,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[5,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[31,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[5,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[32,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[5,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[33,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[5,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[34,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[5,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_fr.iloc[35,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[5,1]
            gender_value["text"] = gender

        # Moustache Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_fr.iloc[36,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[6,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_fr.iloc[37,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[6,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_fr.iloc[38,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[6,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_fr.iloc[39,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[6,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_fr.iloc[40,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[6,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_fr.iloc[41,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[6,1]
            gender_value["text"] = gender

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_fr.iloc[42,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[7,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_fr.iloc[43,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[7,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_fr.iloc[44,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[7,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_fr.iloc[45,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[7,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_fr.iloc[46,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[7,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_fr.iloc[47,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[7,1]
            gender_value["text"] = gender

        # Glasses Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_fr.iloc[48,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[8,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_fr.iloc[49,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[8,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_fr.iloc[50,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[8,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_fr.iloc[51,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[8,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_fr.iloc[52,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[8,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_fr.iloc[53,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[8,1]
            gender_value["text"] = gender

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_fr.iloc[54,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[9,1]
            gender_value["text"] = gender

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_fr.iloc[55,1]
            accuracy["text"] = str(updated_accuracy) + "%"

            gender = self.results_gender.iloc[9,1]
            gender_value["text"] = gender

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_fr.iloc[56,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[9,1]
            gender_value["text"] = gender

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_fr.iloc[57,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[9,1]
            gender_value["text"] = gender

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_fr.iloc[58,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[9,1]
            gender_value["text"] = gender

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_fr.iloc[59,1]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

            gender = self.results_gender.iloc[9,1]
            gender_value["text"] = gender

        else: 
            print(dataset_current)




    def test_btn_full(self, accuracy, updated_accuracy, gender, gender_value, dataset_current, model_current):
        # Non-perturbed Results:
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

        # Light Makeup Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[12,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[14,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[16,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[18,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[20,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[22,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[13,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[15,2]
            accuracy["text"] = str(updated_accuracy) + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[17,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[19,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[21,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Light Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[23,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        # Heavy Makeup Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[0,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[2,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[4,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[6,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[8,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[10,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[1,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[3,2]
            accuracy["text"] = str(updated_accuracy) + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[5,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[7,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[9,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Heavy Makeup)":
            updated_accuracy = self.results_lfw_makeup.iloc[11,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        # Moustache Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[24,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[26,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[28,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[30,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[32,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[34,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[25,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[27,2]
            accuracy["text"] = str(updated_accuracy) + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[29,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[31,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[33,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Moustache)":
            updated_accuracy = self.results_lfw_makeup.iloc[35,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        # Glasses Results: 
        elif model_current == "Facenet512" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[36,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[38,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[40,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[42,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[44,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Male + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[46,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet512" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[37,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "Facenet" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[39,2]
            accuracy["text"] = str(updated_accuracy) + "%"

        elif model_current == "VGG-Face" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[41,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "OpenFace" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[43,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "DeepFace" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[45,2]
            accuracy["text"] = str(updated_accuracy)[:5] + "%"

        elif model_current == "ArcFace" and dataset_current == "LFW (Female + Glasses)":
            updated_accuracy = self.results_lfw_makeup.iloc[47,2]
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




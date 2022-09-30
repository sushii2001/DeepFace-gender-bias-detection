import tkinter as tk

from MyLabel import myLabel
from Buttons import Buttons

class Test_acc_gender:

    # DATASET_VAL = None

    def __init__(self, window, dataset_val, model_menu) -> None:
        self.window = window
        self.dataset_val = dataset_val
        self.model_menu = model_menu
        

    def main(self):

        TEST_VALUE = "0.0%"
        ###### Current Accuracy ######
        accuracy_label = myLabel(self.window, "Accuracy: ", "Helvetica", "#ffffff", "#000000")
        accuracy_value = myLabel(self.window, TEST_VALUE, ("Helvetica", 12), "#12ed96", "#000000")
        accuracy_label.create(x=520, y=180)
        accuracy_value = accuracy_value.create(x=618.5, y=185.2)

        GENDER = None
        ###### Current Gender ######
        genderLabel = myLabel(self.window, "Gender: ", "Helvetica", "#ffffff", "#000000")
        gender_value = myLabel(self.window, GENDER, ("Helvetica", 12), "#ffffff", "#000000")
        genderLabel.create(x=520, y=140)
        gender_value = gender_value.create(x=600, y=144.8)

        # Label for test result
        test_result = myLabel(self.window, "Test Result", "Helvetica", "#ffffff", "#000000")
        test_result.create(x=590, y=105)

        ###### Test Sample button ######
        btn_sample = Buttons(self.window, value=TEST_VALUE)
        sampleButton = tk.Button(
            btn_sample.window,
            text="Test (SAMPLE)",
            bg="yellow",
            fg="black",
            command=lambda: btn_sample.test_btn_sample(accuracy_value, TEST_VALUE, genderLabel, gender_value, self.dataset_val.CURRENT_DATASET, self.model_menu.CURRENT_MODEL),
        )
        sampleButton.place(x=55, y=235)

        ###### Test FULL button ######
        btn_test = Buttons(self.window, value=TEST_VALUE)
        testButton = tk.Button(
            btn_test.window,
            text="Test (FULL)",
            bg="red",
            fg="black",
            command=lambda: btn_test.test_btn_full(accuracy_value, TEST_VALUE, genderLabel, gender_value, self.dataset_val.CURRENT_DATASET, self.model_menu.CURRENT_MODEL),
        )
        testButton.place(x=55, y=265)

        # COMPARISON
        ###### Previous label #######
        prev_label = myLabel(self.window, "Previously Saved", "Helvetica", "#ffffff", "#000000")
        prev_label.create(x=590, y=300) 

        ###### Previous Dataset #######
        prev_dataset_label = myLabel(self.window, "Dataset: ", "Helvetica", "#ffffff", "#000000")
        prev_dataset_label.create(x=520, y=340)
        PREV_DS = ""
        prev_dataset = myLabel(self.window, PREV_DS, ("Helvetica", 10), "#ffffff", "#000000")
        prev_dataset = prev_dataset.create(x=600, y=345)

        ###### Previous Model #######
        prev_model_label = myLabel(self.window, "Model: ", "Helvetica", "#ffffff", "#000000")
        prev_model_label.create(x=520, y=380)
        PREV_MOD = ""
        prev_model = myLabel(self.window, PREV_MOD, ("Helvetica", 12), "#ffffff", "#000000")
        prev_model = prev_model.create(x=590, y=383)

        PREV_ACCURACY_VAL = ""
        ####### Previous Accuracy #######
        prev_accuracy_label = myLabel(self.window, "Accuracy: ", "Helvetica", "#ffffff", "#000000")
        prev_accuracy_value = myLabel(self.window, PREV_ACCURACY_VAL, ("Helvetica", 12), "#ffffff", "#000000")
        prev_accuracy_label.create(x=520, y=420)
        prev_accuracy_value = prev_accuracy_value.create(x=615, y=424)

        ACCURACY_DIFF = "0.0%"
        ####### Accuracy Diff #######
        accuracy_diff_label = myLabel(self.window, "Accuracy Difference: ", "Helvetica", "#ffffff", "#000000")
        accuracy_diff_value = myLabel(self.window, ACCURACY_DIFF, ("Helvetica", 12), "#12ed96", "#000000")
        accuracy_diff_label.create(x=520, y=460)
        accuracy_diff_value = accuracy_diff_value.create(x=710, y=464)

        
        ###### Save button ######
        btn_save = Buttons(self.window, value=TEST_VALUE)
        saveButton = tk.Button(
            btn_save.window,
            text="Save",
            bg="green",
            fg="black",
            command=lambda: btn_save.save_btn(
                prev_accuracy_value, prev_dataset, prev_model, accuracy_value, self.dataset_val.CURRENT_DATASET, self.model_menu.CURRENT_MODEL
            ),
        )
        saveButton.place(x=526, y=235)

        ###### Compare button ######
        btn_compare = Buttons(self.window, value=TEST_VALUE)
        compareButton = tk.Button(
            btn_compare.window,
            text="Compare Previous",
            bg="orange",
            fg="black",
            command=lambda: btn_compare.compare_btn(accuracy_value, prev_accuracy_value, accuracy_diff_value),
        )
        compareButton.place(x=572, y=235)

        ####### Button config #######
        sampleButton.config(height=1, width=12)
        testButton.config(height=1, width=12)

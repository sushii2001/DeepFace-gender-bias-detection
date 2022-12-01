# Import relevant libraries
import unittest
from random import randint

from deepface_main_test_func import *


class TestName(unittest.TestCase):

    """
    Unittest for functions in deepface_main_test_func.py
    """
    
    ####### Test methods #########
    def test_get_name(self):
        """
        Test if input image file into `get_name` returns the image name.

        Args:
            file_name (str): Image file name.
        """

        ####### Positive test case: #######
        positive_file_names = ["Akbar_Hashemi_Rafsanjani_0002.jpg", "Jim_Tressel_0004.jpg", 
                                "Lisa_Marie_Presley_0003.jpg", "Penelope_Ann_Miller_0001.jpg"] 
        positive_output = ["Akbar_Hashemi_Rafsanjani", "Jim_Tressel", "Lisa_Marie_Presley", "Penelope_Ann_Miller"]

        ####### Negative test case: #######
        negative_file_names = ["abc_def_123_", "test.png"]
        negative_output = ["IMAGE: abc_def_123_", "IMAGE: test.png"]

        ##############################
        ####### Test Execution #######
        # Positive test case
        # CASE 1: 
        for file_name, output in zip(positive_file_names, positive_output):
            self.assertEqual(get_name(file_name), output, "\nPossitive case 1: get_name() failed.")
        
        # Negative test case
        # CASE 1: 
        for file_name, output in zip(negative_file_names, negative_output):
            self.assertEqual(get_name(file_name), None, "\nNegative case 1: get_name() failed.")
        ####### Test Execution #######
        ##############################

    def test_find_image(self):
        """
        Test if `find_image` returns the correct image file name.

        Args:
            dataset_path (str): Path to the dataset.
            img_name (str): Image name.
            img_num (int): Image number.
            test_gender (str): Male | Female

        """

        ####### Positive test case: #######
        positive_file_names = [["./data/LFW_gender", "Andrew_Cuomo", "Andrew_Cuomo_0001.jpg", "Male"],
                                ["./data/LFW_gender", "Win_Aung", "Win_Aung_0003.jpg", "Male"],
                                ["./data/LFW_gender", "Corinne_Coman", "Corinne_Coman_0002.jpg", "Female"],
                                ["./data/LFW_gender", "Sally_Field", "Sally_Field_0002.jpg", "Female"]] 

        positive_output = [("./data/LFW_gender/Male/Andrew_Cuomo/Andrew_Cuomo_0001.jpg", "Male"),
                            ("./data/LFW_gender/Male/Win_Aung/Win_Aung_0003.jpg", "Male"),
                            ("./data/LFW_gender/Female/Corinne_Coman/Corinne_Coman_0002.jpg", "Female"),
                            ("./data/LFW_gender/Female/Sally_Field/Sally_Field_0002.jpg", "Female")] 

        ####### Negative test case: #######
        negative_file_names = [["data|data", "non_existance", "non_existance.png", "Female"],
                                [" ", "halo", "halo0003", "Male"],
                                ["./LFW_gender", "bye", "bye_0002.jpg", "Others"],
                                ["./data/LFW_fake", "1235", "xyzj", "Female"]] 

        negative_output = [(None, "Female"),
                            (None, "Male"),
                            (None, "Others"),
                            (None, "Female")] 

        ##############################
        ####### Test Execution #######
        # Positive test case
        # CASE 1: 
        for file_name, output in zip(positive_file_names, positive_output):
            self.assertEqual(find_image(file_name[0], file_name[1], file_name[2], file_name[3]), 
                                output, "\nPossitive case 1: find_image() failed.")
        
        # Negative test case
        # CASE 1: 
        for file_name, output in zip(negative_file_names, negative_output):
            self.assertEqual(find_image(file_name[0], file_name[1], file_name[2], file_name[3]), 
                                output, "\nNegative case 1: find_image() failed.")
        ####### Test Execution #######
        ##############################


    def test_deepface_benchmark_lfw_split(self):
        """
        Test if `deepface_benchmark_lfw_split` returns the correct accuracy.

        Args:
            dataset (str): Dataset name.
            dataset_path (str): Path to the dataset.
            benchmark_df (DataFrame): Benchmark DataFrame.
            model_used (str): Model used.
            METRIC (str): Metric used.
            BACKEND (str): Backend used
            test_gender (str): Male | Female
        """

        # Test instances
        unit_test_df_pos = pd.read_csv('./data/LFW-csv/deepface_unittests.csv')
        unit_test_df_neg = pd.read_csv('./data/LFW-csv/deepface_unittests_neg.csv')
        models = ["Facenet512", "Facenet", "VGG-Face", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
        metrics = "euclidean_l2"
        backends = 'opencv'

        ####### Positive test case: #######
        positive_file_names = [["LFW_gender", "./data/LFW_gender", unit_test_df_pos, models[0], metrics, backends, "Male"],
                                ["LFW_gender", "./data/LFW_gender", unit_test_df_pos, models[0], metrics, backends, "Female"]
                                ] 

        positive_output = [({'Model': 'Facenet512',
                            'Dataset': 'LFW_gender',
                            'CM_ACC': 90.0,
                            'Precision': 83.0,
                            'Recall': 100.0,
                            'Total Images': 10,
                            'Gender': 'Male',
                            'TP': 5,
                            'TN': 4,
                            'FP': 1,
                            'FN': 0,
                            'Undetected': 0}, []),

                            ({'Model': 'Facenet512',
                            'Dataset': 'LFW_gender',
                            'CM_ACC': 90.0,
                            'Precision': 100.0,
                            'Recall': 80.0,
                            'Total Images': 10,
                            'Gender': 'Female',
                            'TP': 4,
                            'TN': 5,
                            'FP': 0,
                            'FN': 1,
                            'Undetected': 0},[])
                        ] 

        ####### Negative test case: #######
        negative_file_names = [["LFW_gender", "./data/LFW_gender", unit_test_df_neg, "Fake Model", metrics, backends, "Male"],
                                ["LFW_gender", "./data/LFW_gender", unit_test_df_neg, models[0], "fake metric", backends, "Female"]
                                ] 

        negative_output = [None, None]

        ##############################
        ####### Test Execution #######
        # Positive test case
        # CASE 1: 
        for file_name, output in zip(positive_file_names, positive_output):
            self.assertEqual(deepface_benchmark_lfw_split(file_name[0], file_name[1], file_name[2], file_name[3], file_name[4], file_name[5], file_name[6]), 
                                output, "\nPossitive case 1: deepface_benchmark_lfw_split() failed.")

        # Negative test case
        # CASE 1:  
        for file_name, output in zip(negative_file_names, negative_output):
            with self.assertRaises(ZeroDivisionError):
                deepface_benchmark_lfw_split(file_name[0], file_name[1], file_name[2], file_name[3], file_name[4], file_name[5], file_name[6])
        ####### Test Execution #######
        ##############################



if __name__.__contains__("__main__"):
    unittest.main()
    
    # To run this test, type in terminal:
    # python .\deepface_unittests.py -b

    # To run pytest, type in terminal:
    # pytest .\deepface_unittests.py -v

    # To run coverage, type in terminal:
    # coverage run .\deepface_unittests.py
    # coverage report -m 

    # To run pytest-cov, type in terminal:
    # pytest --cov=deepface_main_test_func deepface_unittests.py -v
    # To generate HTML report: 
    # pytest --cov=deepface_main_test_func deepface_unittests.py --cov-report=html -v
    # To view the HTML report:
    # open htmlcov/index.html, and run Go Live in VSCode
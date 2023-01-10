# Import relevant libraries and modules
from deepface import DeepFace
import pandas as pd                 
import regex as re
import os

# Deepface functions: 
# [ctrl + f] : to find the function you want to use

# 1. BENCHMARK GENDER SPLIT TESTING
#    - find_image
#    - deepface_benchmark_lfw_split

# 2. BENCHMARK TESTING
#    - deepface_benchmark

# 3. MANUAL TESTING
#   - deepface_get_accuracy
#   - deepface_run_dataset



######## 1. BENCHMARK GENDER SPLIT TESTING ########
def get_name(image_file):
    """
    Function to get the name of the image file
    image_file: the image file to get the name from
    """
    # Initialise the name as None
    name = None


    try:
        # Get the name of the image file with regex
        match = re.search(f"_\d.*\.(jpg|png|jpeg)", image_file)
        name = image_file.replace(match.group(0), "")
        
    except Exception:
        print("IMAGE: " + image_file)
    return name

def find_image(dataset_path, img_name, img_num, test_gender):
    """
    Function to index for the image in the dataset from the CSV file
    dataset_path: the path to the dataset from CSV file
    img_name: the name of the image
    img_num: the number of the image
    test_gender: the gender for this test
    """

    # Initialise the image path with the given paramerters as format: "./dataset_path/img_name_img_num.jpg"
    pathA = f'{dataset_path}/Female/{img_name}/{img_num}'
    pathB = f'{dataset_path}/Male/{img_name}/{img_num}'
    path_truth = None
    gender = test_gender
    
    # Check if the image exists in the dataset in Female folder, returns path and gender 
    if os.path.exists(pathA):
        path_truth = pathA
        gender = 'Female'
    # Check if the image exists in the dataset in Male folder, returns path and gender 
    elif os.path.exists(pathB):
        path_truth = pathB
        gender = 'Male'

    return path_truth, gender


def deepface_benchmark_lfw_split(dataset, dataset_path, benchmark_df, model_used, METRIC, BACKEND, test_gender):
    """
    Deepface function to run the benchmark dataset with gender split
    dataset: the dataset to run
    dataset_path: the path to the dataset
    benchmark_df: the dataframe to store the results
    model_used: the model used for the face recognition
    METRIC: the metric used for the analysis
    BACKEND: the backend used for the face detection and alignment
    test_gender: gender to test
    """

    # Initialise zero to True, False Positive and Negative 
    tp, tn, fp, fn = 0, 0, 0, 0
    # Keep track of the images tested and undetected
    iteration, undetected, perturbed_error = 0, 0, []

    # Loop through the dataframe CSV file to index for the image
    for index, row in benchmark_df.iterrows():
        match_case = row[0]
        
        try:
            # case identification (match or non-match)
            # Positive testing for match case (Image One and Two should be the same person)
            if match_case:
                
                # Get the name of the image file One and Two
                img_name_a = get_name(row[1])
                img_num_1 = row[1]
                img_num_2 = row[2]

                # Get the path of the image file One and Two
                img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender)
                img_path_2, gender_2 = find_image(dataset_path, img_name_a, img_num_2, test_gender)
            
            # Negative testing for non-match case (Image One and Two should not be the same person)
            else:

                # Get the name of the image file One and Two
                img_name_a = get_name(row[1])
                img_name_b = get_name(row[2])
                img_num_1 = row[1]
                img_num_2 = row[2]

                # Get the path of the image file One and Two
                img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender)
                img_path_2, gender_2 = find_image(dataset_path, img_name_b, img_num_2, test_gender)

            # Deepface face recognition test, if current index is the assigned gender test case
            if test_gender == gender_1:
                
                # Track undetected if path is None
                if not (img_path_1 and img_path_2):
                    undetected += 1
                    perturbed_error.append({"img1": img_num_1, "img_path_1": img_path_1, "img2": img_num_2, "img_path_2": img_path_2, "Error": e})

                else:
                    # Run the verification function to check if the images are of the same person
                    verification = DeepFace.verify(img1_path = img_path_1, 
                                                    img2_path = img_path_2, 
                                                    model_name=model_used, 
                                                    enforce_detection=False,
                                                    distance_metric= METRIC, 
                                                    detector_backend = BACKEND)

                    # Store the predicted result and increment the test iteration                              
                    verification_res = verification["verified"]
                    iteration += 1
                    
                    # True Positive if flag and predicted are True:
                    if match_case and verification_res:
                        tp += 1
                    # True Negative if flag and predicted are False:
                    elif match_case == False and verification_res == False:
                        tn += 1

                    # False Positive if flag is False and predicted is True:
                    elif match_case == False and verification_res == True:
                        fp += 1

                    # False Negative if flag is True and predicted is False:
                    elif match_case == True and verification_res == False:
                        fn += 1    

        # Exception handling for undetected images or unexpected errors
        except Exception as e:
            print(e)
            undetected += 1
            perturbed_error.append({"img1": img_num_1, "img_path_1": img_path_1, "img2": img_num_2, "img_path_2": img_path_2, "Error": e})
    
    # calculate confusion matrix:
    cm_acc = round(((tp + tn) / (tp + tn + fp + fn)) * 100, 2) 
    # precision:
    cm_pre = round( ((tp) / (tp + fp)) * 100, 2)
    # recall: 
    cm_rec = round( ((tp) / (tp + fn)) * 100, 2)

    # Return the results as a dictionary and errors encountered as list
    return {"Model": model_used, "Dataset":dataset, "CM_ACC": cm_acc, "Precision":cm_pre, "Recall":cm_rec,\
            "Total Images": iteration, "Gender": test_gender, "TP": tp, "TN":tn, "FP":fp, "FN":fn, "Undetected": undetected}, perturbed_error

         
######## BENCHMARK GENDER SPLIT TESTING ########


# ######## 2. BENCHMARK TESTING ########
# def deepface_benchmark(dataset, dataset_path, benchmark_df, model_used, METRIC, BACKEND):
#     """
#     Deepface function to run the benchmark dataset 
#     dataset: the dataset to run
#     dataset_path: the path to the dataset
#     benchmark_df: the dataframe to store the results
#     model_used: the model used for the face recognition
#     METRIC: the metric used for the analysis
#     BACKEND: the backend used for the face detection and alignment
#     """

#     # Initialise zero to True, False Positive and Negative 
#     tp, tn, fp, fn = 0, 0, 0, 0
#     # Keep track of the images tested and undetected
#     iteration, undetected = 0, 0

#     # Loop through the dataframe CSV file to index for the image
#     for index, row in benchmark_df.iterrows():

#         # If the dataset testing is original benchmark LFW dataset: 
#         if dataset == "LFW":

#             # Check if current iteration is Positive test or Negative test
#             match_case = str(row[3])

#             # If row[3] is "nan", then there is no different person name, hence it is a positive test
#             if match_case == "nan":

#                 # Get name and image number of the image file One and Two
#                 img_name = row["name"]
#                 img_num_1 = f'{row["imagenum1"]:04d}'
#                 img_num_2 = f'{int(row["imagenum2"]):04d}'

#                 # Get the path of the image file One and Two
#                 img_path_1 = f'{dataset_path}/{img_name}/{img_name}_{img_num_1}.jpg'
#                 img_path_2 = f'{dataset_path}/{img_name}/{img_name}_{img_num_2}.jpg'

#                 # Identify current iteration is positive test, increment test iteration
#                 match_case = True
#                 iteration += 1

#             # If row[3] exist value, then there is a different person name, hence it is a negative test
#             else:

#                 # Get name and image number of the image file One and Two
#                 img_name_a = row["name"]
#                 img_num_1 = f'{row["imagenum1"]:04d}'
#                 img_name_b = f'{row["imagenum2"]}'
#                 img_num_2 = f'{int(row[3]):04d}'

#                 # Get the path of the image file One and Two
#                 img_path_1 = f'{dataset_path}/{img_name_a}/{img_name_a}_{img_num_1}.jpg'
#                 img_path_2 = f'{dataset_path}/{img_name_b}/{img_name_b}_{img_num_2}.jpg'

#                 # Identify current iteration is negative test, increment test iteration
#                 match_case = False
#                 iteration += 1
        
#         # If the dataset testing is not original benchmark LFW dataset: (Our custom LFW dataset) 
#         else:

#             # Check if current iteration is Positive test or Negative test
#             match_case = row[0]

#             # Positive testing for match case (Image One and Two should be the same person)
#             if match_case:
#                 # Get name and image number of the image file One and Two
#                 img_name_a = get_name(row[1])
#                 img_num_1 = row[1]
#                 img_num_2 = row[2]

#                 # Get the path of the image file One and Two
#                 img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender=None)
#                 img_path_2, gender_2 = find_image(dataset_path, img_name_a, img_num_2, test_gender=None)
#                 iteration += 1
            
#             # Negative testing for non-match case (Image One and Two should not be the same person)
#             else:

#                 # Get name and image number of the image file One and Two
#                 img_name_a = get_name(row[1])
#                 img_name_b = get_name(row[2])
#                 img_num_1 = row[1]
#                 img_num_2 = row[2]

#                 # Get the path of the image file One and Two
#                 img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender=None)
#                 img_path_2, gender_2 = find_image(dataset_path, img_name_b, img_num_2, test_gender=None)
#                 iteration += 1    

#         try:
#             # Run the verification function to check if the images are of the same person
#             verification = DeepFace.verify(img1_path = img_path_1, 
#                                             img2_path = img_path_2, 
#                                             model_name=model_used, 
#                                             enforce_detection=False,
#                                             distance_metric= METRIC, 
#                                             detector_backend = BACKEND)

#             # Store the predicted result and increment the test iteration
#             verification_res = verification["verified"]
            
#             # Truth Positive if flag and predicted are True:
#             if match_case and verification_res:
#                 tp += 1
#             # Truth Negative if flag and predicted are False:
#             elif match_case == False and verification_res == False:
#                 tn += 1

#             # False Positive if flag is False and predicted is True:
#             elif match_case == False and verification_res == True:
#                 fp += 1

#             # False Negative if flag is True and predicted is False:
#             elif match_case == True and verification_res == False:
#                 fn += 1        

#         # If the face is not detected or unexpected error raised, increment the undetected counter
#         except Exception as e:
#             undetected += 1

#     # calculate confusion matrix:
#     cm_acc = round((tp + tn) / (tp + tn + fp + fn), 2) * 100
#     # precision:
#     cm_pre = round( (tp) / (tp + fp), 2) * 100
#     # recall: 
#     cm_rec = round( (tp) / (tp + fn), 2) * 100

#     # Return the results as a dictionary 
#     return {"Model": model_used, "Dataset":dataset, "CM_ACC": cm_acc, "Precision":cm_pre, "Recall":cm_rec,\
#             "Total Images": iteration, "TP": tp, "TN":tn, "FP":fp, "FN":fn, "Undetected": undetected}

# ######## BENCHMARK TESTING ########



# ######## 3. MANUAL TESTING ########
# def deepface_get_accuracy(img_dir_path, model_used, METRIC, BACKEND) -> dict:
#     """
#     Accuracy function for DeepFace
#     img_dir_path: path to the directory containing the images
#     model_used: the model used for the face recognition
#     METRIC: the metric used for the analysis
#     BACKEND: the backend used for the face detection and alignment
#     """

#     # store the results of each verification:
#     tp, tn, fp, fn = 0, 0, 0, 0
#     image_files = os.listdir(img_dir_path)
#     truth_images = []    
#     false_images = []    
    
#     # If the directory has less than 2 images there is no need to test face recognition
#     if len(image_files) < 2:
#         return {}

#     else:
#         # select the first image 
#         image_1 = f"{img_dir_path}/{image_files[0]}"

#         # loop through the other images and verify if they are the same
#         for img in image_files[1:]:
#             try:
#                 match = re.search(f"_\d.*\.jpg", str(img))
#                 # Find all annotation of the files, replace <NAME> with the desired person to test
#                 # get image name to replace the match string with empty string
#                 # NAME_\d\.jpg
#                 # NAME_\d.*\.jpg
#                 NAME = img.replace(match.group(0), "")
                
#             except AttributeError:
#                 print("IMAGE: " + image_1)
#                 exit(1)

            
#             flag = None
#             if re.search(f"{NAME}_\d.*\.jpg", str(img)):
#                 truth_images.append(img)
#                 flag = True
#             else:
#                 false_images.append(img)    
#                 flag = False

#             try:
#                 img_path = f"{img_dir_path}/{img}"
#                 verification = DeepFace.verify(img1_path = image_1, 
#                                                 img2_path = img_path, 
#                                                 model_name=model_used, 
#                                                 enforce_detection=False,
#                                                 distance_metric= METRIC, 
#                                                 detector_backend = BACKEND)
                                                
#                 verification_res = verification["verified"]
                
#                 # Truth Positive if flag and predicted are True:
#                 if flag and verification_res:
#                     tp += 1
                    
#                 # Truth Negative if flag and predicted are False:
#                 elif flag == False and verification_res == False:
#                     tn += 1

#                 # False Positive if flag is False and predicted is True:
#                 elif flag == False and verification_res == True:
#                     fp += 1

#                 # False Negative if flag is True and predicted is False:
#                 elif flag == True and verification_res == False:
#                     fn += 1        

#             except Exception as e:
#                 print(e)

#         # confusion matrix
#         cm_acc = round((tp + tn) / (tp + tn + fp + fn), 2) * 100

#         return {"cm_acc": cm_acc, "tp": tp, "tn":tn, "fp":fp, "fn":fn, "image_files": len(image_files)-1}


# def deepface_run_dataset(dataset, dataset_path, MODEL, METRIC, BACKEND):
#     """
#     Deepface function to run the dataset and get the accuracy
#     dataset: the dataset to run
#     dataset_path: the path to the dataset
#     MODEL: the model used for the face recognition
#     """

#     avg_truth_pos = 0
#     avg_truth_neg = 0
#     avg_false_pos = 0
#     avg_false_neg = 0
#     total_imgs = 0
    
#     iteration = 0

#     people = os.listdir(dataset_path)
#     for plp in people:

#         img_path = f"{dataset_path}/{plp}"
#         data_res = deepface_get_accuracy(img_path, MODEL, METRIC, BACKEND)

#         if data_res != None:
#             avg_truth_pos += data_res["tp"]
#             avg_truth_neg += data_res["tn"]
#             avg_false_pos += data_res["fp"]
#             avg_false_neg += data_res["fn"]
#             total_imgs += data_res["image_files"]

#             iteration += 1
#             if iteration == 10:
#                 print(img_path)
#                 break

#     # calculate confusion matrix:
#     # accuracy:
#     cm_acc = round((avg_truth_pos + avg_truth_neg) / (avg_truth_pos + avg_truth_neg + avg_false_pos + avg_false_neg), 2) * 100
#     # precision:
#     cm_pre = round( (avg_truth_pos) / (avg_truth_pos + avg_false_pos), 2) * 100
#     # recall: 
#     cm_rec = round( (avg_truth_pos) / (avg_truth_pos + avg_false_neg), 2) * 100


#     return {"Model": MODEL, "Dataset":dataset, "CM_ACC": cm_acc, "Precision":cm_pre, "Recall":cm_rec,"Total Images": total_imgs},\
#          {"TP": avg_truth_pos, "TN":avg_truth_neg, "FP":avg_false_pos, "FN":avg_false_neg}

# ######## MANUAL TESTING ########
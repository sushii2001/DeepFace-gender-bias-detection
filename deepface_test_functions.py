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
    name = None
    try:
        match = re.search(f"_\d.*\.jpg", image_file)
        name = image_file.replace(match.group(0), "")
        
    except Exception:
        print("IMAGE: " + image_file)
    return name

def find_image(dataset_path, img_name, img_num, test_gender):
    pathA = f'{dataset_path}/Female/{img_name}/{img_num}'
    pathB = f'{dataset_path}/Male/{img_name}/{img_num}'
    path_truth = None
    gender = test_gender
    
    if os.path.exists(pathA):
        path_truth = pathA
        gender = 'Female'
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

    tp, tn, fp, fn = 0, 0, 0, 0
    iteration, undetected, perturbed_error = 0, 0, []

    for index, row in benchmark_df.iterrows():
        match_case = row[0]
        
        try:
            # case identification (match or non-match)
            if match_case:
                
                img_name_a = get_name(row[1])
                img_num_1 = row[1]
                img_num_2 = row[2]

                img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender)
                img_path_2, gender_2 = find_image(dataset_path, img_name_a, img_num_2, test_gender)
            
            else:
                img_name_a = get_name(row[1])
                img_name_b = get_name(row[2])
                img_num_1 = row[1]
                img_num_2 = row[2]

                img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender)
                img_path_2, gender_2 = find_image(dataset_path, img_name_b, img_num_2, test_gender)

            # Deepface face recognition test: 
            if test_gender == gender_1:

                if not (img_path_1 and img_path_2):
                    undetected += 1
                    perturbed_error.append({"img1": img_num_1, "img_path_1": img_path_1, "img2": img_num_2, "img_path_2": img_path_2, "Error": e})

                else:
                    # verification = DeepFace.verify(img1_path = img_path_1, img2_path = img_path_2, model_name=MODEL, enforce_detection=False)
                    verification = DeepFace.verify(img1_path = img_path_1, 
                                                    img2_path = img_path_2, 
                                                    model_name=model_used, 
                                                    enforce_detection=False,
                                                    distance_metric= METRIC, 
                                                    detector_backend = BACKEND)
                                                    
                    verification_res = verification["verified"]
                    iteration += 1
                    
                    # Truth Positive if flag and predicted are True:
                    if match_case and verification_res:
                        tp += 1
                    # Truth Negative if flag and predicted are False:
                    elif match_case == False and verification_res == False:
                        tn += 1

                    # False Positive if flag is False and predicted is True:
                    elif match_case == False and verification_res == True:
                        fp += 1

                    # False Negative if flag is True and predicted is False:
                    elif match_case == True and verification_res == False:
                        fn += 1    

        except Exception as e:
            print(e)
            undetected += 1
            perturbed_error.append({"img1": img_num_1, "img_path_1": img_path_1, "img2": img_num_2, "img_path_2": img_path_2, "Error": e})
    
    # calculate confusion matrix:
    cm_acc = round((tp + tn) / (tp + tn + fp + fn), 2) * 100
    # precision:
    cm_pre = round( (tp) / (tp + fp), 2) * 100
    # recall: 
    cm_rec = round( (tp) / (tp + fn), 2) * 100

    return {"Model": model_used, "Dataset":dataset, "CM_ACC": cm_acc, "Precision":cm_pre, "Recall":cm_rec,\
            "Total Images": iteration, "Gender": test_gender, "TP": tp, "TN":tn, "FP":fp, "FN":fn, "Undetected": undetected}, perturbed_error

         
######## BENCHMARK GENDER SPLIT TESTING ########


######## 2. BENCHMARK TESTING ########
def deepface_benchmark(dataset, dataset_path, benchmark_df, model_used, METRIC, BACKEND):
    """
    Deepface function to run the benchmark dataset 
    dataset: the dataset to run
    dataset_path: the path to the dataset
    benchmark_df: the dataframe to store the results
    model_used: the model used for the face recognition
    METRIC: the metric used for the analysis
    BACKEND: the backend used for the face detection and alignment
    """

    tp, tn, fp, fn = 0, 0, 0, 0
    iteration, undetected = 0, 0

    for index, row in benchmark_df.iterrows():

        match_case = row[0]

        if match_case:
            img_name_a = get_name(row[1])
            img_num_1 = row[1]
            img_num_2 = row[2]
            img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender=None)
            img_path_2, gender_2 = find_image(dataset_path, img_name_a, img_num_2, test_gender=None)
            iteration += 1
        
        else:
            img_name_a = get_name(row[1])
            img_name_b = get_name(row[2])
            img_num_1 = row[1]
            img_num_2 = row[2]

            img_path_1, gender_1 = find_image(dataset_path, img_name_a, img_num_1, test_gender=None)
            img_path_2, gender_2 = find_image(dataset_path, img_name_b, img_num_2, test_gender=None)
            iteration += 1    

        try:
            # verification = DeepFace.verify(img1_path = img_path_1, img2_path = img_path_2, model_name=MODEL, enforce_detection=False)
            verification = DeepFace.verify(img1_path = img_path_1, 
                                            img2_path = img_path_2, 
                                            model_name=model_used, 
                                            enforce_detection=False,
                                            distance_metric= METRIC, 
                                            detector_backend = BACKEND)
                                            
            verification_res = verification["verified"]
            
            # Truth Positive if flag and predicted are True:
            if match_case and verification_res:
                tp += 1
            # Truth Negative if flag and predicted are False:
            elif match_case == False and verification_res == False:
                tn += 1

            # False Positive if flag is False and predicted is True:
            elif match_case == False and verification_res == True:
                fp += 1

            # False Negative if flag is True and predicted is False:
            elif match_case == True and verification_res == False:
                fn += 1        

        except Exception as e:
            undetected += 1

    # calculate confusion matrix:
    cm_acc = round((tp + tn) / (tp + tn + fp + fn), 2) * 100
    # precision:
    cm_pre = round( (tp) / (tp + fp), 2) * 100
    # recall: 
    cm_rec = round( (tp) / (tp + fn), 2) * 100


    return {"Model": model_used, "Dataset":dataset, "CM_ACC": cm_acc, "Precision":cm_pre, "Recall":cm_rec,\
            "Total Images": iteration, "TP": tp, "TN":tn, "FP":fp, "FN":fn, "Undetected": undetected}

######## BENCHMARK TESTING ########



######## 3. MANUAL TESTING ########
def deepface_get_accuracy(img_dir_path, model_used, METRIC, BACKEND) -> dict:
    """
    Accuracy function for DeepFace
    img_dir_path: path to the directory containing the images
    model_used: the model used for the face recognition
    METRIC: the metric used for the analysis
    BACKEND: the backend used for the face detection and alignment
    """

    # store the results of each verification:
    tp, tn, fp, fn = 0, 0, 0, 0
    image_files = os.listdir(img_dir_path)
    truth_images = []    
    false_images = []    
    
    # If the directory has less than 2 images there is no need to test face recognition
    if len(image_files) < 2:
        return {}

    else:
        # select the first image 
        image_1 = f"{img_dir_path}/{image_files[0]}"

        # loop through the other images and verify if they are the same
        for img in image_files[1:]:
            try:
                match = re.search(f"_\d.*\.jpg", str(img))
                # Find all annotation of the files, replace <NAME> with the desired person to test
                # get image name to replace the match string with empty string
                # NAME_\d\.jpg
                # NAME_\d.*\.jpg
                NAME = img.replace(match.group(0), "")
                
            except AttributeError:
                print("IMAGE: " + image_1)
                exit(1)

            
            flag = None
            if re.search(f"{NAME}_\d.*\.jpg", str(img)):
                truth_images.append(img)
                flag = True
            else:
                false_images.append(img)    
                flag = False

            try:
                img_path = f"{img_dir_path}/{img}"
                verification = DeepFace.verify(img1_path = image_1, 
                                                img2_path = img_path, 
                                                model_name=model_used, 
                                                enforce_detection=False,
                                                distance_metric= METRIC, 
                                                detector_backend = BACKEND)
                                                
                verification_res = verification["verified"]
                
                # Truth Positive if flag and predicted are True:
                if flag and verification_res:
                    tp += 1
                    
                # Truth Negative if flag and predicted are False:
                elif flag == False and verification_res == False:
                    tn += 1

                # False Positive if flag is False and predicted is True:
                elif flag == False and verification_res == True:
                    fp += 1

                # False Negative if flag is True and predicted is False:
                elif flag == True and verification_res == False:
                    fn += 1        

            except Exception as e:
                print(e)

        # confusion matrix
        cm_acc = round((tp + tn) / (tp + tn + fp + fn), 2) * 100

        return {"cm_acc": cm_acc, "tp": tp, "tn":tn, "fp":fp, "fn":fn, "image_files": len(image_files)-1}


def deepface_run_dataset(dataset, dataset_path, MODEL, METRIC, BACKEND):
    """
    Deepface function to run the dataset and get the accuracy
    dataset: the dataset to run
    dataset_path: the path to the dataset
    MODEL: the model used for the face recognition
    """

    avg_truth_pos = 0
    avg_truth_neg = 0
    avg_false_pos = 0
    avg_false_neg = 0
    total_imgs = 0
    
    iteration = 0

    people = os.listdir(dataset_path)
    for plp in people:

        img_path = f"{dataset_path}/{plp}"
        data_res = deepface_get_accuracy(img_path, MODEL, METRIC, BACKEND)

        if data_res != None:
            avg_truth_pos += data_res["tp"]
            avg_truth_neg += data_res["tn"]
            avg_false_pos += data_res["fp"]
            avg_false_neg += data_res["fn"]
            total_imgs += data_res["image_files"]

            iteration += 1
            if iteration == 10:
                print(img_path)
                break

    # calculate confusion matrix:
    # accuracy:
    cm_acc = round((avg_truth_pos + avg_truth_neg) / (avg_truth_pos + avg_truth_neg + avg_false_pos + avg_false_neg), 2) * 100
    # precision:
    cm_pre = round( (avg_truth_pos) / (avg_truth_pos + avg_false_pos), 2) * 100
    # recall: 
    cm_rec = round( (avg_truth_pos) / (avg_truth_pos + avg_false_neg), 2) * 100


    return {"Model": MODEL, "Dataset":dataset, "CM_ACC": cm_acc, "Precision":cm_pre, "Recall":cm_rec,"Total Images": total_imgs},\
         {"TP": avg_truth_pos, "TN":avg_truth_neg, "FP":avg_false_pos, "FN":avg_false_neg}

######## MANUAL TESTING ########
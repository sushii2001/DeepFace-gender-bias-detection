# DeepFace-gender-bias-detection
An extended investigation on gender bias in DeepFace face recognition model, developed by [Sefik Ilkin Serengil](https://github.com/serengil/deepface)

<p align="center"><img src="./images/deepface-icon-labeled.png" width="200" height="240"></p>

In this experiment, we focus on applying perturbation on the LFW (Labeled Faces in the Wild) benchmark dataset and compare the performance differences between Males and Females. 

# Software Setup
## Package manager (Optional)
It is recommended to have a virtual environment set up so that it separates the dependencies of different projects by creating a separate isolated environment for each project. In our experiment, we use [`Anaconda`](https://www.anaconda.com/products/distribution) to manage it. 

After installing Anaconda or a similar package manager, you may run the code below to create a virtual environment. The "envname" is up to the user to decide and the python version should be at least 3.6 or above. 
```shell
$ conda create -n envname python=x.x anaconda 
```

With the virtual environment created, the user may activate it and continue the setup following the code below: 
```shell
$ conda activate envname
```
To deactivate it simply, 
```shell
$ conda deactivate
```

## Programming Language:
The programming language used in this project is Python, version 3.9.12. You may refer to [`Python`](https://www.python.org/downloads/) for installation details. 

## Face recognition framework:
The download link for deepface framework can be found here [`PyPI`](https://pypi.org/project/deepface/). Alternatively, you may run the code below if you have python pip package installed in your machine. 
```shell
$ pip install deepface
```

## Notebook document
In this project, we use [`Jupyter notebook`](https://jupyter.org/install) as our a web-based interactive computing platform to document our findings and test the Deepface model. 

## Code IDE
We recommend using [`Viusal Studio Code`](https://code.visualstudio.com/download) to run our program, however feel free to use your preferred code editor if you are much familiar with it. 

## Other requirements
The following code installs the other packages' dependency used in this project
```shell
$ pip install -r requirements.txt
```

# Code Components
## `DeepFace-test.ipynb`
This is the notebook responsible for testing the existance of gender bias in Deepface. All test results are saved to the respective CSV files.

1. Import relevant libraries & load data
2. Show Deepface documented results
3. Parameter settings
    - Dataset selection
    - Model selection
    - Metric and Backend configuration
    - Testing gender
4. Deepface test with entire LFW benchmark dataset
5. Deepface test with gender split and perturbed datasets
6. Test results output 
7. Save results to respective CSV files  

## `gui/gui_main.py`
The main script file to launch the project's GUI for users to interact various dataset with state-of-the-art face recognition models. 

1. Dataset and model selection as dropdown menu
2. Sample testing and Full testing buttons
    - Results are output to the respective labels
    - Gender label for single image sample test
    - Accuracy label for both tests 
3. Save and Compare Previous buttons
    - Saves results under the current output 
    - Compares the previously saved accuracy below with current accuracy and outputs the differences

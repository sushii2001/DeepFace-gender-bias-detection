# DeepFace-gender-bias-detection
An extended investigation on gender bias in DeepFace face recognition model, developed by [Sefik Ilkin Serengil](https://github.com/serengil/deepface)

<p align="center"><img src="./images/deepface-icon-labeled.png" width="200" height="240"></p>

In this experiment, we focus on applying perturbation on the [`LFW`](http://vis-www.cs.umass.edu/lfw/) (Labeled Faces in the Wild) benchmark dataset and compare the performance differences between Males and Females. 

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
Please proceed to clone the project repository, and run the following code to install the other packages' dependency used in this project
```shell
$ pip install -r requirements.txt
```

## Data installation
Since GitHub limits the size of files to as large as 50MB, we are unable to include the necessary datasets used in this repository. However, you may refer to this [`GoogleDrive`](https://drive.google.com/drive/folders/1rGlsjHWoje3PFhLIrgCu0pH5NIhvOLdb?usp=sharing) to download it. 

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

# Licence

Deepface is licensed under the MIT License - see [`LICENSE`](https://github.com/serengil/deepface/blob/master/LICENSE) for more details. However, the library wraps some external face recognition models: [VGG-Face](http://www.robots.ox.ac.uk/~vgg/software/vgg_face/), [Facenet](https://github.com/davidsandberg/facenet/blob/master/LICENSE.md), [OpenFace](https://github.com/iwantooxxoox/Keras-OpenFace/blob/master/LICENSE), [DeepFace](https://github.com/swghosh/DeepFace), [DeepID](https://github.com/Ruoyiran/DeepID/blob/master/LICENSE.md), [ArcFace](https://github.com/leondgarse/Keras_insightface/blob/master/LICENSE), [Dlib](https://github.com/davisking/dlib/blob/master/dlib/LICENSE.txt), and [SFace](https://github.com/opencv/opencv_zoo/blob/master/models/face_recognition_sface/LICENSE). Besides, age, gender and race / ethnicity models are based on VGG-Face. Licence types will be inherited if you are going to use those models. Please check the license types of those models for production purposes.

Deepface [logo](https://thenounproject.com/term/face-recognition/2965879/) is created by [Adrien Coquet](https://thenounproject.com/coquet_adrien/) and it is licensed under [Creative Commons: By Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/).

# References:
Serengil, Sefik Ilkin, and Alper Ozpinar. 2021. “HyperExtended
LightFace: A Facial Attribute Analysis Framework.” In *2021
International Conference on Engineering and Emerging Technologies
(ICEET)*, 1–4. IEEE. <https://doi.org/10.1109/ICEET53442.2021.9659697>.

Serengil, Sefik Ilkin, and Alper Ozpinar. 2020. “LightFace: A Hybrid
Deep Face Recognition Framework.” In *2020 Innovations in Intelligent
Systems and Applications Conference (ASYU)*, 23–27. IEEE.
<https://doi.org/10.1109/ASYU50717.2020.9259802>.

Huang, Gary B., Manu Ramesh, Tamara Berg, and Erik Learned-Miller. 2007.
“Labeled Faces in the Wild: A Database for Studying Face Recognition in
Unconstrained Environments.” 07-49. University of Massachusetts,
Amherst.

Pu, M., Kuan, M. Y., Lim, N. T., Chong, C. Y., & Lim, M. K. (2022). Fairness evaluation in
deepfake detection models using metamorphic testing. In 2022 ieee/acm 7th international
workshop on metamorphic testing (met) (pp. 7–14). doi:10.1145/3524846.3527337
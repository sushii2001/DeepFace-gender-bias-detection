import os
import shutil
import re

# MAN: [0-9]+_0_.*
# 30: 30_0_.*

srcpath = "../../../../Monash/C2001-Y3/sem1/FIT3163/others/Assignment/Project-DebFace/DebFace/datasets/UTKFace/Woman"
destpath = "../../../../Monash/C2001-Y3/sem1/FIT3163/others/Assignment/Project-DebFace/DebFace/datasets/UTKFace/Woman/30"

try: 
    for root, subFolders, files in os.walk(srcpath):
        for file in files:
            if bool(re.search("30_1_.*", str(file))):
                shutil.move(os.path.join(root, file), destpath)
except Exception as e:
    print(e)
    print("Error or done")
    exit(1)

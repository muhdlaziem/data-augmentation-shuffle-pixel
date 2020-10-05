import os
import cv2
from main import *
import sys

ROOT_DIR = os.path.abspath(os.curdir)

def generateImagePermutation(perm_no=3 , path=".", proj="Project", seed=None):
    names, images = loadImage(path)
    os.chdir(ROOT_DIR)
    # print(os.curdir)
    if os.path.exists("generated"):
        os.chdir("./generated")
    else:
        os.mkdir("generated")
        os.chdir("./generated")
    
    if(os.path.exists(proj)):
        raise Exception("Project Already exist !")
    else:
        os.mkdir(proj)
        os.chdir(proj)

    for i in range(len(images)):
        permutated = permutate(images[i],num=perm_no, seed=seed)
        print("Writing Permutated " + names[i])

        for j in range(len(permutated)):
            cv2.imwrite(names[i].split(".jpg")[0] + "_" + str(j) + ".jpg", permutated[j])
    
    print("Saved to " + os.getcwd())

if __name__ == "__main__":
    # print(sys.argv[1], sys.argv[2])
    generateImagePermutation(perm_no = int(sys.argv[1]), path=sys.argv[2],proj=sys.argv[3], seed=sys.argv[4])

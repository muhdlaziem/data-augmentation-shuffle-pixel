import os
import cv2
from main import *
import sys
import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--permno", help="amount of permutated image in one image",type=int)
    parser.add_argument("--path", help="Path of folder contains images",type=str)
    parser.add_argument("--proj", help="Project Name",type=str)
    parser.add_argument("--seed", help="Random seed",type=int)
    args = parser.parse_args()
    
    generateImagePermutation(perm_no = args.permno, path=args.path,proj=args.proj, seed=args.seed)

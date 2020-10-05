import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import itertools
import random

def swapPixel(X,Y):
    X = X ^ Y
    Y = X ^ Y
    X = X ^ Y
    return (X, Y)

def permutate(img, num=3, seed=10):
    random.seed(seed)
    img_perm=[]
    IMG_PIXEL = [img[0:421,0:297], img[0:421, 297:594], img[421:842,0:297], img[421:842, 297:594]]
    LAST_COLUMN = img[:, 594:]
    PERMUTATIONS = list(itertools.permutations(IMG_PIXEL))
    del PERMUTATIONS[7] # this permutation resulting same image as original
    for i in range(num):
        perm = random.choice(PERMUTATIONS)
        arr = np.array(perm)
        arr[0], arr[1] = swapPixel(arr[0], arr[1])
        arr[2], arr[3] = swapPixel(arr[2], arr[3])
        row1 = cv2.hconcat([arr[0],arr[1]])
        row2 = cv2.hconcat([arr[2],arr[3]])
        IMG = cv2.vconcat([row1,row2])
        IMG = cv2.hconcat([IMG,LAST_COLUMN])
        # print(IMG.shape)
        img_perm.append(IMG)
    # showImage(img_perm)
    return np.array(img_perm)

def showImage(imgs):
    i = 0
    for img in imgs:
        cv2.imshow("img" + str(i), img)
        i += 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resizeImage(img):
    img = cv2.resize(img, (595, 842),  interpolation = cv2.INTER_AREA) 
    return img

def loadImage(path):
    os.chdir(path)
    imgs = []
    names = []
    print("Loading images...")
    for name in os.listdir():
        if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.jpeg'):
            img = cv2.imread(name)
            names.append(name)
            # print(name)
            img = resizeImage(img)
            imgs.append(img)
    print("Amount of images: " + str(len(imgs)))
    return names, imgs


if __name__ == "__main__":
    pass
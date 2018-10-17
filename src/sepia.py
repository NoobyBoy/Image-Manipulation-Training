#-*- conding utf-8 -*-

from __future__ import print_function
from PIL import Image
from black_and_white import *
import os


"""
This module contain the function:

-sepia :
    add a sépia effect on the picture,
    the effect is not very a sepia effect and is very slow because of
    black_and_white function ... meh...

"""

def sepia(img, variation=(45,10,10)):
    """
    The function change the image in black_and_white and augment red parameter
    acording to red_augmentation
    """

    img.paste(img.convert("L"))
    px = img.load()

    size_x, size_y = img.size

    for y in range(size_y):
        for x in range(size_x):
            ppx = px[x,y]
            new = (ppx[0] + variation[0], ppx[1] + variation[1], ppx[2] + variation[2])
            px[x,y] = new




if __name__ == "__main__":
    img = Image.open("../image/merge_conflict.jpg")
    print ("Sepia: \n")
    sepia(img)
    img.show()
    os.system("pause")

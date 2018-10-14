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

def sepia(img, red_augmentation):
    """
    The function change the image in black_and_white and augment red parameter
    acording to red_augmentation
    """

    black_and_white(img)

    R,G,B = img.split()

    
    R = R.point(lambda i : i + red_augmentation)
    mask = Image.merge("RGB", (R,G,B))

    img.paste(mask)



if __name__ == "__main__":
    img = Image.open("../image/wtf.jpg")
    sepia(img, 40)
    img.show()
    print ("Sepia: \n")
    os.system("pause")

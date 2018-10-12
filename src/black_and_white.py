#-*- conding utf-8 -*-


from __future__ import print_function
from PIL import Image
from statistics import mean
import os

"""
This module contain the print_function:

-black_and_white :
    Transform the image passed as parameter in a black and white Image,
    it work pretty well but is very looow...
    Have to find a way to do it faster

"""


def black_and_white(img):
    """
    for each pixel of the img the average of it's RGB component is applied to
    each RGB component wich result in a darker or brighter grey
    """

    px = img.load()
    size_x, size_y = img.size


    for y in range (size_y):
        for x in range (size_x):
            average = int(mean(px[x,y]))
            px[x,y] = (average, average, average)




if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    black_and_white(img)
    img.show()
    print ("Black and White : \n")
    os.system("pause")

#-*- conding utf-8 -*-


from __future__ import print_function
from PIL import Image
from statistics import mean
import os


def black_and_white(img):

    px = img.load()
    size_x, size_y = img.size


    for y in range (size_y):
        for x in range (size_x):
            average = int(mean(px[x,y]))
            px[x,y] = (average, average, average)





if __name__ == "__main__":
    img = Image.open("../image/space.jpg")
    black_and_white(img)
    print ("Black and White : \n")
    os.system("pause")

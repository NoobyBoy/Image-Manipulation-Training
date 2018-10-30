#-*- conding utf-8 -*-

from __future__ import print_function
from PIL import Image, ImageChops
import os

def find_image(img, img2, percentage=100):

    if percentage <= 0 or percentage > 100:
        raise ValueError("Percentage value must stick betwen 0 and 100 (0 not included)")

    size_x, size_y = img.size
    len_x, len_y = img2.size

    for y in range(size_y):
        for x in range(size_x):
            tmp = img.crop((x, y, x + len_x, y + len_y))
            res = ImageChops.difference(tmp, img2).getbbox()
            if res is None:
                return x, y, x + len_x, y + len_y



if __name__ == "__main__":
    img = Image.open("../image/spidey.jpg")
    img2 = Image.open("../image/crop.jpg")
    print ("Find Image : \n")
    find_image(img, img2)
    #img.show()
    os.system("pause")

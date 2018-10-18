#-*- conding utf-8 -*-

import unittest
import sys
import os

sys.path.append("..\\src")

from shuffling import *

class TestShuffling(unittest.TestCase):

    def test_shuffling(self):
        img = Image.open("../image/spidey.jpg")
        img2 = Image.open("../image/spidey.jpg")
        img3 = Image.open("../image/spidey.jpg")

        size_x, size_y = img.size

        shuffling(img2, 10)
        shuffling(img3, 10)


        #very slow way to test but testing each pixel independently is not
        # a good idea (some pixel may be identical but the picture is
        #  not the same)
        l1 = []
        l2 = []
        l3 = []
        for y in range(size_y):
            for x in range(size_x):
                l1.append(img.getpixel((x,y)))
                l2.append(img2.getpixel((x,y)))
                l3.append(img3.getpixel((x,y)))
            self.assertNotEqual(l1, l2)
            self.assertNotEqual(l1, l3)
            self.assertNotEqual(l2, l3)
            l1 = []
            l2 = []
            l3 = []


if __name__ == '__main__':
    unittest.main()

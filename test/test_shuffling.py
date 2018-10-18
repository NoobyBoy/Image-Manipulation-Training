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

        px = img.load()
        px2 = img2.load()
        px3 = img3.load()

        self.assertEqual(px, px2)
        self.assertEqual(px, px3)
        self.assertEqual(px2, px3)

        shuffling(img2, 10)
        shuffling(img3, 10)

        px2 = img2.load()
        px3 = img3.load()

        #The probability that one of them are equal is veeeeery low
        self.assertNotEqual(px, px2)
        self.assertNotEqual(px, px3)
        self.assertNotEqual(px2, px3)


if __name__ == '__main__':
    unittest.main()

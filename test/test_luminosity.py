#-*- conding utf-8 -*-

import unittest
import sys
import os

sys.path.append("..\\src")

from luminosity import *


class LuminosityTest(unittest.TestCase):

    def test_bad_parameter(self):

        with self.assertRaises(TypeError):
            luminosity_variation()
            luminosity_variation("img", "value")

    def test_luminosity_variation(self):

        img = Image.open("../image/spidey.jpg")
        img2 = Image.open("../image/spidey.jpg")
        img3 = Image.open("../image/spidey.jpg")
        x,y = img.size

        luminosity_variation(img, 50)
        luminosity_variation(img2, -50)
        luminosity_variation(img3, 100, True)

        px = img.load()
        px2 = img.load()
        px3 = img3.load()

        for i in range (y):
            for j in range (x):
                print(j,i, px2[j,i])
                self.assertTrue(px[j,i] >= (50, 50, 50))
                self.assertTrue(px2[j,i] <= (205, 205, 205))
                self.assertEqual(px3[j,i], (255,255,255))


    def test_luminosity_percentage(self):

                img = Image.open("../image/spidey.jpg")
                img_clean = img.copy()
                img2 = Image.open("../image/spidey.jpg")
                img3 = Image.open("../image/spidey.jpg")
                x,y = img.size

                luminosity_percentage(img, 50)
                luminosity_percentage(img2, 0)
                luminosity_percentage(img3, 100)

                px = img.load()
                px_clean = img_clean.load()
                px2 = img.load()
                px3 = img3.load()

                for i in range (y):
                    for j in range (x):
                        print(j,i, px2[j,i])
                        self.assertTrue(px[j,i], px_clean[j,i])
                        self.assertTrue(px2[j,i], (0, 0, 0))
                        self.assertEqual(px3[j,i], (255,255,255))

if __name__ == '__main__':
    unittest.main()

#-*- conding utf-8 -*-

from __future__ import print_function
from PIL import Image
import os


def image_list_to_gif(img_list, name="new_gif.gif", duration=100, loop_mode=0):

    if not name.endswith(".gif"):
        name += ".gif"

    img_list[0].save(name, save_all=True, append_images=img_list[1:],
                        duration=duration, loop=loop_mode)


if __name__ == "__main__":
    import shuffling
    img_list = []
    print("Image list to gif : \n")
    img = Image.open("../image/spidey.jpg")
    for n in range(10):
        tmp = img.copy()
        shuffling.shuffling(tmp, 10)
        img_list.append(tmp)

    image_list_to_gif(img_list, "test")
    os.system("pause")
    os.remove("test.gif")

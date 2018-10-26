#! /usr/bin/env python3
#-*- conding utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import os

class MyDialogGif:

    def __init__(self, parent):

        self.top = Toplevel(parent)
        self.top.grab_set()
        self.top.title("Make your GIF")

        self.all_types = [("All Files", ".*"), ("JPEG",".jpg .jpeg"),
            ("PNG", ".png"),("BMP", ".bmp"), ("GIF", ".gif")]
        self.result = (None, None, None, None)
        self.img_list = []
        self.path = ""
        self.duration = 100
        self.loop_mode = 0
        self.all_files = pd.DataFrame(index=["Name","Image","ImageTk"])

        self.can_but = Canvas(self.top)

        self.can_img = Canvas(self.can_but, width=150, height=150, bg="white")
        self.but_add = Button(self.can_but, text="Add Picture(s) to selection",
                                command=self.add_files)
        self.lab_dur = Label(self.can_but, text="Duration of each frame\n(milliseconds) :")
        self.ent_dur = Entry(self.can_but, width=5)
        self.lab_loop = Label(self.can_but, text="Number of loop\n (0 = infinite) :")
        self.ent_loop = Entry(self.can_but, width=5)
        self.but_save = Button(self.can_but, text="Save GIF")
        self.but_cancel = Button(self.can_but, text="Cancel", command=self.top.destroy)

        self.ent_dur.insert(0, str(self.duration))
        self.ent_loop.insert(0, str(self.loop_mode))

        self.can_img.grid(column=1, row=0, padx=5, pady=5, columnspan=2)
        self.but_add.grid(column=1, row=1, padx=5, pady=10, columnspan=2)
        self.lab_dur.grid(column=1, row=2, pady=5, sticky="E")
        self.ent_dur.grid(column=2, row=2, padx=10, pady=5, sticky="W")
        self.lab_loop.grid(column=1, row=3, pady=5, sticky="E")
        self.ent_loop.grid(column=2, row=3, padx=10, pady=5, sticky="W")
        self.but_save.grid(column=1, row=5, padx=5, pady=5, sticky="N")
        self.but_cancel.grid(column=2, row=5, padx=5, pady=5, sticky="N")

        self.can_but.grid(column=3, row=1, sticky="NS", padx=5, pady=5)


        self.yscroll = ttk.Scrollbar(self.top, orient=VERTICAL)
        self.yscroll.grid(column=2, row=1, sticky="NS")

        self.res_box = Listbox(self.top, width=50, height=23,
                                yscrollcommand=self.yscroll.set)
        self.res_box.grid(column=1, row=1, padx=10, pady=10)

        self.yscroll.config(command=self.res_box.yview)

    def add_files(self):
        files = self.path = filedialog.askopenfilenames(filetype=self.all_types)

        for file in files:
            img = Image.open(file)
            imgtk = ImageTk.PhotoImage(img)
            name = os.path.basename(file)
            self.all_files = self.all_files.append(
                {"Name":name, "Image":img, "ImageTk":imgtk}, ignore_index=True)

        print(self.all_files)


    def save(self):
        pass


if __name__ == '__main__':

    root = Tk()
    d = MyDialogGif(root)
    root.wait_window(d.top)

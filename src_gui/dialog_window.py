#-*- conding utf-8 -*-

from tkinter import *

class MyDialogThresholding:

    def __init__(self, parent):

        self.top = Toplevel(parent)
        self.top.grab_set()
        self.top.title("Choose the component")

        self.answer = None

        R = lambda : self.choose("R")
        G = lambda : self.choose("G")
        B = lambda : self.choose("B")
        All = lambda : self.choose("All")

        self.txt = Label(self.top, text="Choose the component of the picture\n you want to do the effect")
        self.txt.grid(column=0, row=0, columnspan=4)

        self.but_R = Button(self.top, text="Red", command=R)
        self.but_G = Button(self.top, text="Green", command=G)
        self.but_B = Button(self.top, text="Blue", command=B)
        self.but_All = Button(self.top, text="All", command=All)
        self.but_Cancel = Button(self.top, text="Cancel", command=self.top.destroy)

        self.but_R.grid(column=0, row=1, padx=6, pady=10)
        self.but_G.grid(column=1, row=1, padx=6)
        self.but_B.grid(column=2, row=1, padx=6)
        self.but_All.grid(column=3, row=1, padx=6)
        self.but_Cancel.grid(column=0, row=2, columnspan=4,
                            sticky="EW", padx=5, pady=5)

    def choose(self, answer):

        self.answer = answer
        self.top.destroy()


if __name__ == '__main__':

    root = Tk()
    d = MyDialogThresholding(root)
    root.wait_window(d.top)

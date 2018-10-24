#-*- conding utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk
#my modules
from src.black_and_white import *
from src.luminosity import *
from src.negative import *
from src.pixelisation import *
from src.sepia import *
from src.shuffling import *
from src.thresholding import *

class Gui(Frame):

    def __init__(self, win, **kwargs):
        self.win = win
        Frame.__init__(self, self.win, width=300, height=200, **kwargs)
        self.win.protocol("WM_DELETE_WINDOW", self.win.quit)
        self.pack()

        self.path = ""
        self.img = None
        self.imgTk = None
        self.all_types = [("All Files", ".*"), ("JPEG",".jpg .jpeg"),
            ("PNG", ".png"),("BMP", ".bmp"), ("GIF", ".gif")]

        #Menu Creation
        self.menu = Menu(self)

        self.menu_file = Menu(self.menu, tearoff=0)
        self.menu_file.add_command(label="Load", command=self.load)
        self.menu_file.add_command(label="Save", command=self.save)
        self.menu_file.add_command(label="Save As", command=self.save_as)
        self.menu_file.add_command(label="Exit", command=self.quit)

        self.menu.add_cascade(label="File", menu=self.menu_file)
        win.config(menu=self.menu)

        #Button

        self.but_baw = Button(self, text="Black & White", command=self.black_and_white)
        self.but_lum = Button(self, text="Luminosity", command=self.luminosity)
        self.but_neg = Button(self, text="Negative", command=self.negative)
        self.but_pix = Button(self, text="Pixelisation", command=self.pixelisation)
        self.but_sepia = Button(self, text="Sepia", command=self.sepia)
        self.but_shuffle = Button(self, text="Shuffling", command=self.shuffling)
        self.but_thresh= Button(self, text="Thresholding", command=self.thresholding)

        self.but_baw.grid(column=0, row=1, sticky="W", pady=5)
        self.but_lum.grid(column=0, row=2, sticky="W", pady=5)
        self.but_neg.grid(column=0, row=3, sticky="W", pady=5)
        self.but_pix.grid(column=0, row=4, sticky="W", pady=5)
        self.but_sepia.grid(column=0, row=5, sticky="W", pady=5)
        self.but_shuffle.grid(column=0, row=6, sticky="W", pady=5)
        self.but_thresh.grid(column=0, row=7, sticky="W", pady=5)

        #Image
        self.lab_img = Label(self)
        self.lab_img.grid(column=1, row=1, pady=4, rowspan=8)

    def save(self):
        if self.img and self.path:
            self.img.save(self.path)

    def save_as(self):
        if sys.platform.startswith('win'):
            messagebox.showwarning("Warning", """On Windows the file extension is not autimatically added
                and should be added by the hand""")
        self.path = filedialog.asksaveasfilename(filetypes=self.all_types)
        self.save()

    def load(self):
        self.path = filedialog.askopenfilename(filetype=self.all_types)
        if self.path:
            self.img = Image.open(self.path)
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.lab_img["image"] = self.imgTk

    def black_and_white(self):
        if self.img:
            black_and_white(self.img)
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.lab_img["image"] = self.imgTk


    def luminosity(self):
        #test of simpledialog
        if self.img:
            answer = simpledialog.askinteger("Input", "Percentage :",
                                    minvalue=0, maxvalue=100)
            if answer:
                pass
            else:
                pass

    def negative(self):
        if self.img:
            negative(self.img)
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.lab_img["image"] = self.imgTk

    def pixelisation(self):
        if self.img:
            size = simpledialog.askinteger("Input", "Size of pixelisation :",
                                    minvalue=2)
            if size:
                pixelisation(self.img, size)
                self.imgTk = ImageTk.PhotoImage(self.img)
                self.lab_img["image"] = self.imgTk

    def sepia(self):
        pass

    def shuffling(self):
        if self.img:
            size = simpledialog.askinteger("Input", "Size of croping :",
                                    minvalue=2)
            if size:
                shuffling(self.img, size)
                self.imgTk = ImageTk.PhotoImage(self.img)
                self.lab_img["image"] = self.imgTk

    def thresholding(self):
        pass


def main():
        print("main")

        win = Tk()
        a = Gui(win)
        a.mainloop()
        a.destroy()


main()

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

        self.but_baw = Button(self, text="Black & White")
        self.but_lum = Button(self, text="Luminosity", command=self.luminosity)
        self.but_neg = Button(self, text="Negative")
        self.but_pix = Button(self, text="Pixelisation")
        self.but_sepia = Button(self, text="Sepia")
        self.but_shuffle = Button(self, text="Shuffling")
        self.but_thresh= Button(self, text="Thresholding")

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
        self.img = Image.open(self.path)
        self.imgTk = ImageTk.PhotoImage(self.img, size="400,400")
        self.lab_img["image"] = self.imgTk


    def luminosity(self):
        #test of simpledialog
        answer = simpledialog.askinteger("Input", "Percentage :",
                                 parent=self, minvalue=0, maxvalue=100)
        if answer is not None:
            print("Your age is ", answer)
        else:
            print("You don't have an age?")



def main():
        print("main")

        win = Tk()
        a = Gui(win)
        a.mainloop()
        a.destroy()


main()

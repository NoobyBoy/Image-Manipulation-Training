#-*- conding utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import colorchooser
from PIL import ImageTk
#my modules
from src_gui.dialog_window import *
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

        self.history = []
        self.pos = 0
        self.path = ""
        self.idir = "image"
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

        self.menu_edit = Menu(self.menu, tearoff=0)
        self.menu_edit.add_command(label="Undo", command=self.undo)
        self.menu_edit.add_command(label="Redo", command=self.redo)
        self.menu_edit.add_command(label="Original", command=self.original)
        self.menu_edit.add_command(label="Actual", command=self.actual)

        self.menu_help = Menu(self.menu, tearoff=0)
        self.menu_help.add_command(label="?")
        self.menu_help.add_command(label="About")

        self.menu.add_cascade(label="File", menu=self.menu_file)
        self.menu.add_cascade(label="Edit", menu=self.menu_edit)
        self.menu.add_cascade(label="Help", menu=self.menu_help)
        win.config(menu=self.menu)

        #Button
        self.but_baw = Button(self, text="Black & White", command=self.black_and_white)
        self.but_lum = Button(self, text="Luminosity", command=self.luminosity)
        self.but_neg = Button(self, text="Negative", command=self.negative)
        self.but_pix = Button(self, text="Pixelisation", command=self.pixelisation)
        self.but_sepia = Button(self, text="Sepia", command=self.sepia)
        self.but_shuffle = Button(self, text="Shuffling", command=self.shuffling)
        self.but_thresh= Button(self, text="Thresholding", command=self.thresholding)

        self.but_baw.grid(column=0, row=1, sticky="WN", pady=5, padx=5)
        self.but_lum.grid(column=1, row=1, sticky="WN", pady=5, padx=5)
        self.but_neg.grid(column=2, row=1, sticky="WN", pady=5, padx=5)
        self.but_pix.grid(column=3, row=1, sticky="WN", pady=5, padx=5)
        self.but_sepia.grid(column=4, row=1, sticky="WN", pady=5, padx=5)
        self.but_shuffle.grid(column=5, row=1, sticky="WN", pady=5, padx=5)
        self.but_thresh.grid(column=6, row=1, sticky="WN", pady=5, padx=5)

        #Image
        self.lab_img = Label(self)
        self.lab_img.grid(column=0, row=2, pady=4, columnspan=8)

        #Event
        self.bind_all("<Control-KeyPress-z>", self.undo)
        self.bind_all("<Control-KeyPress-y>", self.redo)
        self.bind_all("<Control-KeyPress-o>", self.load)
        self.bind_all("<Control-KeyPress-s>", self.save)
        self.bind_all("<Control-Shift-KeyPress-s>", self.save_as)

        #temporary because I don't know why but open/save window is broken sometime
        self.path = "image\\back.jpeg"
        if self.path:
            self.img = Image.open(self.path)
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.lab_img["image"] = self.imgTk
            self.history = [self.img.copy()]
            self.pos = 0

    def modification(self):
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.lab_img["image"] = self.imgTk
        self.pos += 1
        del self.history[self.pos:len(self.history)]
        self.history.append(self.img.copy())

    def undo(self, *evt):
        try :
            if self.pos > 0:
                self.pos -= 1
                self.img = self.history[self.pos].copy()
                self.imgTk = ImageTk.PhotoImage(self.img)
                self.lab_img["image"] = self.imgTk

        except IndexError:
            self.pos += 1

    def redo(self, *evt):
        try :
            self.pos += 1
            self.img = self.history[self.pos].copy()
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.lab_img["image"] = self.imgTk

        except IndexError:
            self.pos -= 1

    def original(self):
        try:
            self.pos = 0
            self.imgTk = ImageTk.PhotoImage(self.history[0])
            self.lab_img["image"] = self.imgTk
        except IndexError:
            pass

    def actual(self):
        try:
            self.pos = len(self.history) - 1
            self.imgTk = ImageTk.PhotoImage(self.history[-1])
            self.lab_img["image"] = self.imgTk
        except IndexError:
            pass

    def save(self, *evt):
        if self.img and self.path:
            try:
                self.img.save(self.path)
            except:
                if sys.platform.startswith('win'):
                    messagebox.showerror("Error", "No extension to the file (On Windows: even if you select the extension you have to add it by hand)")
                else:
                    messagebox.showerror("Error", "No extension to the file")

    def save_as(self, *evt):
        if sys.platform.startswith('win'):
            messagebox.showwarning("Warning", """On Windows the file extension is not autimatically added
                and should be added by hand""")
        self.path = filedialog.asksaveasfilename(filetypes=self.all_types)
        self.save()

    def load(self, *evt):
        self.path = filedialog.askopenfilename(filetype=self.all_types,
                                    initialdir=self.idir)
        if self.path:
            self.img = Image.open(self.path)
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.lab_img["image"] = self.imgTk
            self.history = [self.img.copy()]
            self.pos = 0

    def black_and_white(self):
        if self.img:
            black_and_white(self.img)
            self.modification()


    def luminosity(self):
        if self.img:
            dialog = MyDialogLuminosity(self)
            self.wait_window(dialog.top)
            answer = dialog.answer
            if answer == "Var":
                var = simpledialog.askinteger("Input", "Variation [-255 ; 255] :",
                                        minvalue=-255, maxvalue=255)
                if var:
                    luminosity_variation(self.img, var)
                    self.modification()
            elif answer == "Per":
                perc = simpledialog.askinteger("Input", "Percentage :",
                                        minvalue=0, maxvalue=100)
                if perc:
                    luminosity_percentage(self.img, perc)
                    self.modification()

    def negative(self):
        if self.img:
            negative(self.img)
            self.modification()

    def pixelisation(self):
        if self.img:
            size = simpledialog.askinteger("Input", "Size of pixelisation :",
                                    minvalue=2)
            if size:
                pixelisation(self.img, size)
                self.modification()

    def sepia(self):
        if self.img:
            answer = messagebox.askyesnocancel("Choose", "Do you want to use the default value (it's advisable)")

            if answer:
                sepia(self.img)
                self.modification()

            elif answer is False:
                color = colorchooser.askcolor()
                if None not in color:
                    color = (int(color[0][0]), int(color[0][1]), int(color[0][2]))
                    sepia(self.img, color)
                    self.modification()


    def shuffling(self):
        if self.img:
            size = simpledialog.askinteger("Input", "Size of croping :",
                                    minvalue=2)
            if size:
                shuffling(self.img, size)
                self.modification()

    def thresholding(self):
        if self.img:
            dialog = MyDialogThresholding(self)
            self.wait_window(dialog.top)
            answer = dialog.answer
            if answer:
                threshold = simpledialog.askinteger("Input", "threshold",
                                            minvalue=0, maxvalue=255)
                if threshold:
                    thresholding(self.img, threshold, answer)
                    self.modification()


def main():
        print("main")

        win = Tk()
        a = Gui(win)
        a.mainloop()
        a.destroy()


main()

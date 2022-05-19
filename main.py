import os
from tkinter import *
from PIL import ImageTk, Image

class App:
    def __init__(self, root, papka):
        self.papka = papka
        self.root = root
        self.root.geometry("700x600")
        p = os.getcwd()
        os.chdir(p + self.papka)
        p = os.getcwd()
        self.spisok = os.listdir(p)
        self.l = 0
        self.r = 1
        #imgs
        self.im = Image.open(self.spisok[self.l])
        self.im = ImageTk.PhotoImage(self.im)
        self.im_lbl = Label(self.root, image=self.im)
        self.im_lbl.pack(side='left')
        self.imr = Image.open(self.spisok[self.r])
        self.imr = ImageTk.PhotoImage(self.imr)
        self.imr_lbl = Label(self.root, image=self.imr)
        self.imr_lbl.pack(side='right')
        #btns
        self.b1 = Button(self.root, text="left", command=self.left)
        self.b1.place(x=0, y=454)
        self.b2 = Button(self.root, text="right", command=self.right)
        self.b2.place(x=635, y=454)
        self.btn_new = Button(self.root, text='New', command=self.menu)
        self.btn_exit = Button(self.root, text='Exit', command=self.root.destroy)
        #txts
        self.txt = Text(self.root, height=20, width=80)
        self.txt_lbl = Label(self.root, text='Here is your #1 Book!')

    def menu(self):
        pass
    def top_book(self):
        pass

    def top_movie(self):
        pass

    def left(self):
        if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
            self.imr_lbl.after(1000, self.imr_lbl.destroy())
            self.b2.destroy()
            self.b1.destroy()
            self.im_lbl.pack(side='top')
            self.txt_lbl.pack(side='bottom')
            self.btn_new.pack(side='left')
            self.btn_exit.pack(side='right')

        if self.r < self.l:
            self.r = self.l + 1
            self.imr = Image.open(self.spisok[self.r])
            self.imr = ImageTk.PhotoImage(self.imr)
            self.imr_lbl.config(image=self.imr)
        else:
            self.r += 1
            self.imr = Image.open(self.spisok[self.r])
            self.imr = ImageTk.PhotoImage(self.imr)
            self.imr_lbl.config(image=self.imr)

    def right(self):
        if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
            self.im_lbl.after(1000, self.im_lbl.destroy())
            self.b1.destroy()
            self.b2.destroy()
            self.imr_lbl.pack(side='top')
            self.txt_lbl.pack(side='bottom')
            self.btn_new.pack(side='left')
            self.btn_exit.pack(side='right')

        if self.l < self.r:
            self.l = self.r + 1
            self.im = Image.open(self.spisok[self.l])
            self.im = ImageTk.PhotoImage(self.im)
            self.im_lbl.config(image=self.im)
        else:
            self.l += 1
            self.im = Image.open(self.spisok[self.l])
            self.im = ImageTk.PhotoImage(self.im)
            self.im_lbl.config(image=self.im)



root = Tk()
root.resizable(width=False, height=False)
ob = App(root, '/topbooks')
root.mainloop()

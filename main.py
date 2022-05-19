import os
from tkinter import *
from PIL import ImageTk, Image
class Open:
    def __init__(self, root):
        self.root = root
        ##self.root.title("Yes/No")
        ##self.root.iconbitmap(r'images/converted-icon.ico')
        self.root.geometry('750x450')
        self.font = Image.open(r"images/font.png")
        self.font = ImageTk.PhotoImage(self.font)
        ##bg = PhotoImage(file=r"images/font.png")
        self.start_btn_image = Image.open(r"images/start.png")
        self.start_btn_image = ImageTk.PhotoImage(self.start_btn_image)
        ##start_btm_image = PhotoImage(file=r"images/start.png")
        self.label = Label(root, image=self.font, bg='#0f0f0f')
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        Button(self.root,image=self.start_btn_image,borderwidth=0, bg='#0f0f0f').pack(pady=15,side='bottom')
        #start_btm = Button(root, image=start_btm_image, command=start(), borderwidth=0, bg='#0f0f0f')
        #start_btm.pack(pady=15, side=BOTTOM)
    ### command start
    def start(self):

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
        self.im = Image.open(self.spisok[self.l])
        self.im = ImageTk.PhotoImage(self.im)
        self.im_lbl = Label(self.root, image=self.im)
        self.im_lbl.pack(side='left')
        self.imr = Image.open(self.spisok[self.r])
        self.imr = ImageTk.PhotoImage(self.imr)
        self.imr_lbl = Label(self.root, image=self.imr)
        self.imr_lbl.pack(side='right')
        Button(self.root, text="left", command=self.left).pack(pady=5,side='left')
        Button(self.root, text="right", command=self.right).pack(pady=5, side='right')
    def left(self):
        if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
            pass
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
            pass
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
game = Open(root)
##ob = App(root, '/topbooks')
root.mainloop()

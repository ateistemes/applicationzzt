import tkinter as tk
from PIL import Image, ImageTk
import os

LARGEFONT = ("Verdana", 35)


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def open_frame(self):
        self.lift()


class TopBooks(App):
   def __init__(self, *args, **kwargs):
       App.__init__(self, *args, **kwargs)

       self.papka = "/topbooks"
       p = os.getcwd()
       os.chdir(p + self.papka)
       p = os.getcwd()
       self.spisok = os.listdir(p)
       self.l = 0
       self.r = 1

       #img left
       self.im = Image.open(self.spisok[self.l])
       self.im = ImageTk.PhotoImage(self.im)
       self.im_lbl = tk.Label(self, image=self.im, bg="#D4BAEC")
       self.im_lbl.image = self.im
       self.im_lbl.pack(side="left")

       #img right
       self.img = Image.open(self.spisok[self.r])
       self.img = ImageTk.PhotoImage(self.img)
       self.img_lbl = tk.Label(self, image=self.img, bg="#D4BAEC")
       self.img_lbl.image=self.img
       self.img_lbl.pack(side="right")

       #buttons
       self.btn_left = tk.Button(self, text="Left", command=lambda: self.left())
       self.btn_left.place(x=0, y=454)
       #self.btn_left = tk.Button(self, text="Left", command=lambda: self.left())
       #self.btn_left.pack(side="left")

       #self.btn_right = tk.Button(self, text="Right", command=lambda: self.right())
       #self.btn_right.pack(side="right")
       self.btn_right = tk.Button(self, text="Right", command=lambda: self.right())
       self.btn_right.place(x=635, y=454)

       self.label = tk.Label(self, text="Pick only one!", font=LARGEFONT)
       self.label.place(x = 200, y= 10)

   def right(self):
       if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
           self.im_lbl.after(1000, self.im_lbl.destroy())
           self.btn_left.destroy()
           self.btn_right.destroy()
           self.label.destroy()
           self.img_lbl.pack(side='top')

       if self.l < self.r:
           self.l = self.r + 1
           self.im = Image.open(self.spisok[self.l])
           self.im = ImageTk.PhotoImage(self.im)
           self.im_lbl.image=self.im
           self.im_lbl.config(image=self.im)
       else:
           self.l += 1
           self.im = Image.open(self.spisok[self.l])
           self.im = ImageTk.PhotoImage(self.im)
           self.im_lbl.image=self.im
           self.im_lbl.config(image=self.im)
   def left(self):
       if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
           self.img_lbl.after(1000, self.img_lbl.destroy())
           self.btn_left.destroy()
           self.btn_right.destroy()
           self.label.destroy()

           #self.bks_lbl.destroy()
           self.im_lbl.pack(side='top')

       if self.r < self.l:
           self.r = self.l + 1
           self.img = Image.open(self.spisok[self.r])
           self.img = ImageTk.PhotoImage(self.img)
           self.img_lbl.image = self.img
           self.img_lbl.config(image=self.img)
       else:
           self.r += 1
           self.img = Image.open(self.spisok[self.r])
           self.img = ImageTk.PhotoImage(self.img)
           self.img_lbl.image=self.img
           self.img_lbl.config(image=self.img)





class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = App(self)
        p2 = TopBooks(self)

        btn_frame = tk.Frame(self)
        container = tk.Frame(self)
        btn_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(btn_frame, text="menu", command=p1.open_frame)
        b2 = tk.Button(btn_frame, text="top books", command=p2.open_frame)

        b1.pack(side="top")
        b2.pack(side="top")
        p1.open_frame()

root = tk.Tk()
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("700x700")
root.mainloop()

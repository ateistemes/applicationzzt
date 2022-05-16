import tkinter as tk
import os
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import Button, OUTSIDE
root = tk.Tk()
canvas = tk.Canvas(root, height=800, width=700, bg='grey')


p = os.getcwd()

os.chdir(p + '/top_books')
path = os.getcwd()
print(path)
spisok = os.listdir(path)

def left():
    pass
def right():
    pass

i= 1
while i<len(spisok):
    picture = Image.open(spisok[i])
    picture = ImageTk.PhotoImage(picture)
    label = tk.Label(root, image=picture)
    label.pack(side='left')
    image = Image.open(spisok[i+1])
    image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image = image)
    label.pack(side='right')
    break

btn = Button(root, text='Left', bd=10, command=left())
btn.place(x=10, y=450)
btn2 = Button(root, text='Right', bd=10, command=right())
btn2.place(x=570, y=450)
root.mainloop()

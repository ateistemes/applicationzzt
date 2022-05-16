import tkinter as tk
import os
from PIL import ImageTk, Image

root = tk.Tk()
canvas = tk.Canvas(root, height=800, width=700, bg='grey')


p = os.getcwd()

os.chdir(p + '/kartinki')
path = os.getcwd()
print(path)
spisok = os.listdir(path)
i = 0
while i < len(spisok):
    picture = Image.open(spisok[i])
    picture = ImageTk.PhotoImage(picture)
    label = tk.Label(root, image=picture)
    label.pack(side='left')
    image = Image.open(spisok[i+1])
    image = ImageTk.PhotoImage(image)
    label = tk.Label(root, image = image)
    label.pack(side='right')
    break

root.mainloop()


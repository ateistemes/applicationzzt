from tkinter import  *
from PIL import ImageTk, Image
# tk window initialization
root = Tk()
root.title("Yes/No")
root.iconbitmap(r"C:\Users\zhasm\Desktop\converted-icon.ico")
root.geometry('750x450')
'''root.eval('tk::PlaceWindow . center')'''

# Variable initialization
bg = PhotoImage(file=r"C:\Users\zhasm\Desktop\font.png")
start_btm_image = PhotoImage(file=r"C:\Users\zhasm\Desktop\rsz_start_btm.png")

# Starting window
label = Label(root, image=bg, bg='#0f0f0f')
label.place(x=0, y=0, relwidth=1, relheight=1)

'''text = Label(root, text='Let\'s play', font=('Helvetica', 20))
text.pack(pady=200)'''

# Functions
def start():
    label1 = Label(root, bg='white')
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    text = Label(label1, text='Let\'s play', font=('Helvetica', 20))
    text.pack(pady=200)




# Buttons
start_btm = Button(root, image=start_btm_image, command=start(), borderwidth=0)
start_btm.pack(pady=15, side=BOTTOM)


'''root.bind('<Configure>', resizer)'''
root.mainloop()
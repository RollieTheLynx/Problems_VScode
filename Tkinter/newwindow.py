"""
Created on Wed May 13 21:10:06 2020

@author: Rollie
"""
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ass")
root.iconbitmap("icon.ico")
root.geometry("400x400")

vertical = Scale(root, from_=0, to = 200)
vertical.pack()

horizontal = Scale(root, from_=0, to = 200, orient = HORIZONTAL)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()


root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:10:06 2020

@author: Rollie
"""
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("ass")
root.iconbitmap("icon.ico")

frame = LabelFrame(root, text = "My frame", padx = 100, pady = 100)
frame.pack(padx=10, pady = 10)

b = Button(frame, text = "Dont")
b.pack()
b2 = Button(frame, text = "Do")
b.grid(row=0, column = 0)
b2.grid(row=0, column = 1)


root.mainloop()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
The complete list of leap years in the first half of the 21st century is therefore 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, and 2048
"""
from tkinter import *

root = Tk()

#create a label widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "Cruel world!")
myLabel3 = Label(root, text = "Cruel jews!")

#shove label on screen
myLabel1.grid(row=0, column = 0)
myLabel2.grid(row=1, column = 5)
myLabel3.grid(row=1, column = 1)

root.mainloop()
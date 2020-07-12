# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

e= Entry(root, borderwidth=5)
e.pack()
e.insert(0,"Enter name")

def myClick():
    myLabel = Label(root, text= e.get())
    myLabel.pack()
    
myButton = Button(root, text = "Enter your name!", command = myClick, fg="blue", bg="#000000")
myButton.pack()

root.mainloop()
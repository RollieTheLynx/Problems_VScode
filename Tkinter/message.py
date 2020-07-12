"""
Created on Wed May 13 21:10:06 2020

@author: Rollie
"""
from tkinter import *
#from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("ass")
root.iconbitmap("icon.ico")

def popup():
    response = messagebox.askyesno("Title", "Hello nigger")
    Label(root, text=response).pack()
#showinfo , showerror, askquestion, askokcancel, askyesno


Button(root, text = "Popup", command=popup).pack()













root.mainloop()

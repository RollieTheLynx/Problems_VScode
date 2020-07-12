from tkinter import *

root = Tk()
root.title("Calculator v1")

e= Entry(root, width = 35, borderwidth=5)
e.grid(row=0, column = 0, columnspan= 3, padx=10, pady=10)  

def numClick(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(num))
    
def clearClick():
    e.delete(0,END)
    
def addClick():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)
    
def minusClick():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)
    
def multiClick():
    first_number = e.get()
    global f_num
    global math
    math = "multi"
    f_num = int(first_number)
    e.delete(0, END)
    
def divideClick():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)
    
def equalClick():
    second_number=e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0,f_num + int(second_number))
    if math == "sub":
        e.insert(0,f_num - int(second_number))
    if math == "multi":
        e.insert(0,f_num * int(second_number))
    if math == "div":
        e.insert(0,f_num / int(second_number))
    

myButton7 = Button(root, text = "7", command = lambda: numClick(7), padx=40, pady=20)
myButton7.grid(row = 1, column = 0)

myButton8 = Button(root, text = "8", command = lambda: numClick(8), padx=40, pady=20)
myButton8.grid(row = 1, column = 1)

myButton9 = Button(root, text = "9", command = lambda: numClick(9), padx=40, pady=20)
myButton9.grid(row = 1, column = 2)

myButton4 = Button(root, text = "4", command = lambda: numClick(4), padx=40, pady=20)
myButton4.grid(row = 2, column = 0)

myButton5 = Button(root, text = "5", command = lambda: numClick(5), padx=40, pady=20)
myButton5.grid(row = 2, column = 1)

myButton6 = Button(root, text = "6", command = lambda: numClick(6), padx=40, pady=20)
myButton6.grid(row = 2, column = 2)

myButton1 = Button(root, text = "1", command = lambda: numClick(1), padx=40, pady=20)
myButton1.grid(row = 3, column = 0)

myButton2 = Button(root, text = "2", command = lambda: numClick(2), padx=40, pady=20)
myButton2.grid(row = 3, column = 1)

myButton3 = Button(root, text = "3", command = lambda: numClick(3), padx=40, pady=20)
myButton3.grid(row = 3, column = 2)

myButton0 = Button(root, text = "0", command = lambda: numClick(0), padx=40, pady=20)
myButton0.grid(row = 4, column = 0)

myButtonClear = Button(root, text = "Clear", command = clearClick, padx=29, pady=20)
myButtonClear.grid(row = 4, column = 1)

myButtonEquals = Button(root, text = "=", command = equalClick, padx=39, pady=20)
myButtonEquals.grid(row = 4, column = 2)

myButtonPlus = Button(root, text = "+", command = addClick, padx=40, pady=20)
myButtonPlus.grid(row = 5, column = 0)

myButtonMinus = Button(root, text = "-", command = minusClick, padx=40, pady=20)
myButtonMinus.grid(row = 5, column = 1)

myButtonMulti = Button(root, text = "*", command = multiClick, padx=40, pady=20)
myButtonMulti.grid(row = 5, column = 2)

myButtonDivide = Button(root, text = "/", command = divideClick, padx=40, pady=20)
myButtonDivide.grid(row = 5, column = 3)

root.mainloop()
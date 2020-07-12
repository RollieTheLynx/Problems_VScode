# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:01:55 2020

@author: Rollie
"""


from tkinter import *
from PIL import ImageTk,Image
import openpyxl
import datetime

root = Tk()
root.title('Форма заказа пицыы')
root.iconbitmap('mc.ico')

#%%
thickness_frame = LabelFrame(root, padx=100, text = "Толщина")
thickness_frame.grid(row = 0, column = 0, padx=10, pady=10)

thickness_choice = StringVar()
thickness_choice.set("Толстое тесто")


btn1 = Radiobutton(thickness_frame, text="Толстое тесто", variable=thickness_choice, value="Толстое тесто").grid(row = 0, column = 0)
btn2 = Radiobutton(thickness_frame, text="Тонкое тесто", variable=thickness_choice, value="Тонкое тесто").grid(row = 0, column = 1)

#%%
topping_frame = LabelFrame(root, padx=100, text = "Начинка")
topping_frame.grid(row = 1, column = 0, padx=10, pady=10)

toppings = [
	"Итальянская", 
	"Европейская", 
	"Барбекю"
    ]	

topping_choice = StringVar()
topping_choice.set(toppings[0])

toppingsMenu = OptionMenu(topping_frame, topping_choice, *toppings)
toppingsMenu.pack()



#%%
diameter_frame = LabelFrame(root, padx=100, text = "Диаметр")
diameter_frame.grid(row = 2, column = 0, padx=10, pady=10)
diam_slider = Scale(diameter_frame, from_=20, to=60, orient=HORIZONTAL)
diam_slider.pack()


#%%
#more checkbox options

options_frame = LabelFrame(root, padx=100, text = "Опции")
options_frame.grid(row = 3, column = 0, padx=10, pady=10)

oversize_choice = StringVar()

slice_box = Checkbutton(options_frame, text="Нарезать", variable = oversize_choice, onvalue = "Нарезать", offvalue = "Не нарезать")
slice_box.deselect()
slice_box.pack()


#%%

totals_frame = LabelFrame(root, padx=100, pady=50, text = "Итог")
totals_frame.grid(row = 4, column = 0, padx=10, pady=10)



myButton = Button(totals_frame, text="Готово!", command=lambda: sumitup(thickness_choice.get(), topping_choice.get(), diam_slider.get(), oversize_choice.get()))
myButton.grid(row = 0, column = 0)


def sumitup(thickness_choice, topping_choice, diam_slider, oversize_choice):
    global totalsLabel
    totalsLabel = Label(totals_frame, text = "")
    totalsLabel.configure(text = thickness_choice + '\n' + topping_choice + '\n' + str(diam_slider) + ' см\n' + oversize_choice)
    totalsLabel.grid(row = 1, column = 0)
    popup(thickness_choice, topping_choice, diam_slider, oversize_choice)	
#%%
def popup(thickness_choice, topping_choice, diam_slider, oversize_choice):
    response = messagebox.askquestion("Экспорт", "Экспортировать заказ в Excel?")
    if response == "yes":
        try:
            wb = openpyxl.load_workbook("orders_export.xlsx")
            sheet = wb.active
        except FileNotFoundError:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet["A1"] = "Дата и время заказа"
            sheet["B1"] = "Толщина"
            sheet["C1"] = "Начинка"
            sheet["D1"] = "Диаметр"
            sheet["E1"] = "Нарезать?"
        
        now = datetime.datetime.now()
        new_row = (now.strftime("%Y-%m-%d %H:%M:%S"), thickness_choice, topping_choice, diam_slider, oversize_choice)
        sheet.append(new_row)

        wb.save('orders_export.xlsx')
	



#%%

root.mainloop()

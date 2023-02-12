# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:47:47 2020

@author: Rollie
"""


import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\Rollie\\Desktop\\Таблица поиска.xlsx')
first_sheet = wb.get_sheet_names()[0]
worksheet = wb.get_sheet_by_name(first_sheet)

#here you iterate over the rows in the specific column
for row in range(2,worksheet.max_row+1):  
    for column in "M":  #Here you can add or reduce the columns
        cell_name = "{}{}".format(column, row)
        if worksheet[cell_name].value is not None:
            worksheet[cell_name].value = '/'.join(worksheet[cell_name].value.split('/')[:-2]) + '/projects/' + worksheet[cell_name].value.split('/')[-2]

wb.save('C:\\Users\\Rollie\\Desktop\\Таблица поиска_processed.xlsx')
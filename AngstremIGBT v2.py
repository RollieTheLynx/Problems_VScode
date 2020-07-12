# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:40:54 2020

@author: Rollie
"""
import requests
from bs4 import BeautifulSoup
import openpyxl

result = requests.get("https://www.angstrem.ru/ru/catalog/silovye-poluprovodnikovye-pribory/igbt-moduli") 

#print(result.status_code)

src = result.content

soup = BeautifulSoup(src, "html.parser") #"lxml"?

table = soup.find("table") #находим первую таблицу

table_rows = table.find_all("tr") #находим в ней строки

wb = openpyxl.Workbook() #создаем Excel
sheet = wb.active

for tr in table_rows:
     td = tr.find_all("td") #в каждом ряду tr находим колонки td
     row = [i.text for i in td] #складываем лист row из td
     sheet.append(row) #вносим в эксель row

wb.save("Angstrem_IGBT v2.xlsx")




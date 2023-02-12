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

headers = {}
rows = soup.find_all("tr")
thead = soup.find("thead").find_all("th")

for i in range(len(thead)):
     headers[i] = thead[i].text.strip().lower()

data = []

for row in rows:
     cells = row.find_all("td")

item = {}

for index in headers:
     item[headers[index]] = cells[index].text
     data.append(item)
     
#%%
print(data)

wb = openpyxl.Workbook()
sheet = wb.active

def headerLine(a_dict): 
    list = [] 
    for key in a_dict.keys(): 
        list.append(key) 
          
    sheet.append(list)

def dataLine(a_dict, device): 
    list = [] 
    for value in a_dict[device].values(): 
        list.append(value) 
          
    sheet.append(list)

headerLine(data[0])

for i in range(0,len(data)):
    dataLine(data,i)

wb.save("Angstrem_IGBT.xlsx")



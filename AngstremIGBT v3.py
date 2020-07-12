# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:40:54 2020

@author: Rollie
"""
import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas
from time import sleep

wb = openpyxl.Workbook() #создаем Excel
sheet = wb.active

def scrapePage(link):
    dataframes = pandas.read_html(link)
    n = 1
    for dataframe in dataframes:
        dataframe.to_excel("Angstrem_IGBT v3 page " + str(n) + ".xlsx")
        n += 1
        
#%%
    sleep(3)
    result = requests.get("https://www.angstrem.ru/ru/catalog/silovye-poluprovodnikovye-pribory/igbt-moduli") 
    src = result.content
    soup = BeautifulSoup(src, "html.parser") #"lxml"?
    
    button = soup.find( "a", {"title":"На следующую страницу"} )
    link = "https://www.angstrem.ru" + button['href']
    scrapePage(link)
    
    
#%%
link = "https://www.angstrem.ru/ru/catalog/silovye-poluprovodnikovye-pribory/igbt-moduli"
scrapePage(link)





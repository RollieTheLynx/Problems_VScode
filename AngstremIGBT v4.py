# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:40:54 2020

@author: Rollie
"""
import requests
from bs4 import BeautifulSoup
import pandas
from time import sleep

def scrapePage(link):
    response = requests.get(link)
    #print(response.status_code)

    soup = BeautifulSoup(response.content, "html.parser")
   
    table = soup.find("table", class_ = "views-table cols-6") #находим таблицу
    table_rows = table.find_all("tr") #находим в ней строки
    
    headers = [] # список с заголовками из th
    t_head = table_rows[0].find_all("th")
    for x in range(0,len(t_head)):
        headers.append(t_head[x].get_text())
    
    devices = [] #список с подсписками для каждого прибора
    t_body = soup.find_all("tr") #строки тела таблицы
    for line in range(1,len(t_body)):
        new_device = [] 
        new_row = t_body[line].find_all("td")
        for y in range(0,len(new_row)):
            new_device.append(new_row[y].get_text())
        devices.append(new_device)
    
    names = [item[0] for item in devices]
    vces = [item[0] for item in devices]
    ics = [item[0] for item in devices]
    vcesats = [item[0] for item in devices]
    ips = [item[0] for item in devices]
    topos = [item[0] for item in devices]
    
    excel = pandas.DataFrame({
        headers[0]: names,
        headers[1]: vces,
        headers[2]: ics,
        headers[3]: vcesats,
        headers[4]: ips,
        headers[5]: topos
        })
   
    
#lst2 = [item[0] for item in devices]

    
    excel.to_excel("Angstrem v4.xlsx") 

    try:
        find_Button()
    except:

#%%
def find_Button():
    button = soup.find( "a", {"title":"На следующую страницу"} )
    link = "https://www.angstrem.ru" + button['href']
    return link
    
    
    
#%%
link = "https://www.angstrem.ru/ru/catalog/silovye-poluprovodnikovye-pribory/igbt-moduli"
scrapePage(link)



# writer = pd.ExcelWriter('c:/temp/test.xlsx', engine='openpyxl')

# In [49]: df.to_excel(writer, index=False)

# In [50]: df.to_excel(writer, startrow=len(df)+2, index=False)

# In [51]: writer.save()





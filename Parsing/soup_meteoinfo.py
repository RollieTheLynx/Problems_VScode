# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:15:47 2021

@author: TN90072
"""

import requests
from bs4 import BeautifulSoup

result = requests.get("https://meteoinfo.ru/forecasts/russia/oryol-area/orel")

#print(result.status_code)

#print(result.headers)

src = result.content

#print(src)

soup = BeautifulSoup(src, "lxml")

table = soup.find("table",{"class":"fc_tab_1"})

rows = table.find_all("tr")

data = []

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    
for day in range(len(data[0])):
    print(data[0][day] + ": " + data[2][day + 1])


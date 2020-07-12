# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:54:37 2020

@author: Rollie

https://wiki.eveuniversity.org/API_access_to_market_data
"""

import csv
import json
import requests

#%% https://www.fuzzwork.co.uk/resources/typeids.csv
with open('typeids.csv', newline='', encoding='utf-8', mode='r') as ids_file:
    reader = csv.reader(ids_file)
    for row in ids_file:
        IDs = {rows[0]:rows[1] for rows in reader}

#%% https://api.evemarketer.com/ec/marketstat?typeid=215&usesystem=30000142 returns the market data for Iron Charge S (typeid 215) for Jita (usesystem 30000142)

lookie = input('Enter item name: ')

# list out keys and values separately 
key_list = list(IDs.keys()) 
val_list = list(IDs.values()) 
  
lookieID = (key_list[val_list.index(lookie)])  
url = "https://api.evemarketer.com/ec/marketstat/json?typeid=" + str(lookieID) + "&usesystem=30000142"

try:
    api_request = requests.get(url)
    example = json.loads(api_request.content)
except Exception:
    print("Error...")

#%%
print('Item ID:', lookieID)
print('Item name:', lookie)
print('Sell volume:', example[0]["sell"]["volume"])
print('Sell average:', example[0]["sell"]["avg"])
print('Sell stddev:', example[0]["sell"]["stdDev"])
print('Sell median:', example[0]["sell"]["median"])
print('Sell percentile:', example[0]["sell"]["fivePercent"])
print('Sell max:', example[0]["sell"]["max"])
print('Sell min:', example[0]["sell"]["min"])



#https://esi.evetech.net/ui/#/Market/get_markets_prices !!!!!!!!!!!!!
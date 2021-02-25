# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:57:52 2021

@author: TN90072

https://esi.evetech.net/ui/

"""

import requests 

#id = 94881232
# GET /characters/{character_id}/

url = 'https://esi.evetech.net/latest/characters/94881232/'
response = requests.get(url)

# print(response.headers)
print(response.text)

#%%
import requests
import json 

# https://www.adam4eve.eu/info_locations.php
# lonetrek 10000016
# /markets/{region_id}/orders/

url = 'https://esi.evetech.net/latest/markets/10000016/orders/'
response = requests.get(url)

orders = json.loads(response.content)

for order in range(len(orders)):
    print(orders[order]["order_id"])

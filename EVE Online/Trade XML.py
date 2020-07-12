# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:54:37 2020

@author: Rollie

https://wiki.eveuniversity.org/API_access_to_market_data
"""

import xml.etree.ElementTree as ET
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
    print(example)
except Exception:
    print("Error...")


#%%   systems ID: 30003135 - D-PNP9, 30000142 - Jita
example = '''
<exec_api version="2.0" method="marketstat_xml">
    <marketstat>
        <type id="215">
            <buy>
            <volume>11110000</volume>
            <avg>4.65</avg>
            <stddev>0.84</stddev>
            <median>4.58</median>
            <percentile>4.68</percentile>
            <max>4.68</max>
            <min>3.09</min>
            </buy>
            
            <sell>
            <volume>21049264</volume>
            <avg>8.41</avg>
            <stddev>5.66</stddev>
            <median>8.49</median>
            <percentile>5.17</percentile>
            <max>22.50</max>
            <min>5.14</min>
            </sell>
        </type>
        
        <type id="216">
            <buy>
            <volume>10800000</volume>
            <avg>1.06</avg>
            <stddev>0.10</stddev>
            <median>1.05</median>
            <percentile>1.22</percentile>
            <max>1.22</max>
            <min>1.05</min>
            </buy>
            
            <sell>
            <volume>9141303</volume>
            <avg>6.63</avg>
            <stddev>2.84</stddev>
            <median>7.98</median>
            <percentile>5.93</percentile>
            <max>10.99</max>
            <min>3.99</min>
            </sell>
        </type>
    </marketstat>
</exec_api>'''

#%%
stuff = ET.fromstring(example)
types = stuff.findall('marketstat/type')
print('Item IDs:', len(types), "\n")

for item in types:
    print('Item ID:', item.get('id'))
    print('Item name:', IDs[str(item.get('id'))])
    print('Sell volume:', item.find('sell/volume').text)
    print('Sell average:', item.find('sell/avg').text)
    print('Sell stddev:', item.find('sell/stddev').text)
    print('Sell median:', item.find('sell/median').text)
    print('Sell percentile:', item.find('sell/percentile').text)
    print('Sell max:', item.find('sell/max').text)
    print('Sell min:', item.find('sell/min').text)
    print()   
    
    
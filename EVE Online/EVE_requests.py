# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:57:52 2021
@author: TN90072
https://esi.evetech.net/ui/
"""
import requests
import json
import csv
import pandas as pd
import os
import sys


with open(os.path.join(sys.path[0], "EVE Online\\typeids.csv"), "r", encoding='utf-8') as id_data:
    id_dict = {}
    for line in csv.reader(id_data):
        id_dict[int(line[0])] = line[1]

#%%
# получаем список систем из API - очень долго
# GET /universe/systems/
url = 'https://esi.evetech.net/latest/universe/systems/'
response = requests.get(url)
systems_ids = json.loads(response.content)
solar_dict = {}
counter = 1
for system in systems_ids:
    url = 'https://esi.evetech.net/latest/universe/systems/{}/?datasource=tranquility&language=en'.format(system)
    response = requests.get(url)
    system_info = json.loads(response.content)
    solar_dict[system] = system_info["name"]
    print("Doing {} of {}".format(counter, len(systems_ids)))
    counter += 1
with open('EVE Online\\system_ids.txt', 'w') as f:
    print(solar_dict, file=f)

#%%
# или загружаем готовый из файла

with open(os.path.join(sys.path[0], "EVE Online\\solar_systems.csv"), "r", encoding='utf-8-sig') as solar_data:
    solar_dict = {}
    for line in csv.reader(solar_data):
        solar_dict[int(line[0])] = line[1]

# GET /universe/structures/
with open(os.path.join(sys.path[0], "EVE Online\\NPC_stations.csv"), "r", encoding='utf-8-sig') as npc_data:
    npc_stations_dict = {}
    for line in csv.reader(npc_data):
        npc_stations_dict[int(line[0])] = line[1]
        
with open(os.path.join(sys.path[0], "EVE Online\\player_structures.csv"), "r", encoding='utf-8-sig') as player_data:
    player_stations_dict = {}
    for line in csv.reader(player_data):
        player_stations_dict[int(line[0])] = line[1]


#%%

def char_info(character_id):
    ''' Get character's public information
    id = 94881232
    GET /characters/{character_id}/
    '''

    url = 'https://esi.evetech.net/latest/characters/{}/'.format(character_id)
    response = requests.get(url)
    # print(response.headers)
    char_info = json.loads(response.content)
    print(char_info["name"])


char_info(94881232)

#%%
# https://www.adam4eve.eu/info_locations.php
# lonetrek 10000016
# Aridia 10000054
# /markets/{region_id}/orders/

def market_orders(region_id):
    
    def make_call(page_no):
        url = 'https://esi.evetech.net/latest/markets/{}/orders/?datasource=tranquility&order_type=all&page={}'.format(region_id, page)
        response = requests.get(url)
        orders = json.loads(response.content)
        new_df = pd.json_normalize(orders)
        print(url)
        return new_df
    
    page = 1
    df = pd.DataFrame()
    additional = make_call(page)
    df = df.append(additional)

    while len(additional) == 1000:
        page +=1
        additional = make_call(page)
        df = df.append(additional)
    
    pd.set_option('display.max_columns', None)
    df.reset_index(inplace=True)
    df['type_name'] = df['type_id'].map(id_dict)
    df['system_name'] = df['system_id'].map(solar_dict)
    df['location_name'] = df['location_id'].map(npc_stations_dict)
    df['price_max'] = df.groupby(['type_name'])['price'].transform(max)
    df['price_min'] = df.groupby(['type_name'])['price'].transform(min)
    df["status"] = ["buy order" if ele  == "True" else "sell order" for ele in df["is_buy_order"]]
    # https://stackoverflow.com/questions/30953299/pandas-if-row-in-column-a-contains-x-write-y-to-row-in-column-b
    df.to_excel("EVE Online\\output.xlsx")
    return df


    # для каждого уникального ИД найти заказ на продажу с минимальной ценой и заказ на  покупку с максимальной ценой и посчитать прибыль
    # resulting_df = df['type_name'].copy().drop_duplicates()
    # https://stackoverflow.com/questions/15741759/find-maximum-value-of-a-column-and-return-the-corresponding-row-values-using-pan
    # # print(resulting_df.head(5))

df = market_orders(10000054)

#df2 = df['type_name'].copy().drop_duplicates().to_frame() # unique goods


#%%
# Pandas Pivot table
# lab3 In [29]
df_gptest = df[['type_name','is_buy_order','price']]
grouped_test1 = df_gptest.groupby(['type_name','is_buy_order'],as_index=False).max()
grouped_test1
grouped_test1.to_excel("EVE Online\\grouped.xlsx")

grouped_pivot = grouped_test1.pivot(index='type_name',columns='is_buy_order')
grouped_pivot
grouped_pivot.to_excel("EVE Online\\pivot.xlsx")

#%%
df.dropna(inplace=True)

database = {}
for index, row in df.iterrows():
    if row['type_name'] not in database:
        if row['is_buy_order'] == True:
            database[row['type_name']] = {'highest_buy_order': row['price'], 'lowest_sell_order': None}
        else:
            database[row['type_name']] = {'lowest_sell_order': row['price'], 'highest_buy_order': None}
            
    else:
        if row["is_buy_order"] == True:
            if database[row["type_name"]]['highest_buy_order'] == None:
                database[row["type_name"]]['highest_buy_order'] = row["price"]
            if row["price"] > database[row["type_name"]]['highest_buy_order']:
                database[row["type_name"]]['highest_buy_order'] = row["price"]
        if row["is_buy_order"] == False:
            if database[row["type_name"]]['lowest_sell_order'] == None:
                database[row["type_name"]]['lowest_sell_order'] = row["price"]                
            if row["price"] < database[row["type_name"]]['lowest_sell_order']:
                database[row["type_name"]]['lowest_sell_order'] = row["price"]

            
df.loc[df['type_name'] == 'Arbalest Compact Light Missile Launcher']

for key in database:
    try:
        if database[key]['highest_buy_order'] > database[key]['lowest_sell_order']:
            print("{}: the lowest_sell_order is {} and highest_buy_order is {}".format(key, database[key]['lowest_sell_order'], database[key]['highest_buy_order']))
    except TypeError:
            continue

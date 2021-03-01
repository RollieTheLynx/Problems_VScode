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


with open(os.path.join(sys.path[0], "Documents\Python Scripts\\typeids.csv"), "r", encoding='utf-8') as id_data:
    id_dict = {}
    for line in csv.reader(id_data):
        id_dict[int(line[0])] = line[1]

# GET /universe/systems/
with open(os.path.join(sys.path[0], "Documents\Python Scripts\\solar_systems.csv"), "r", encoding='utf-8-sig') as solar_data:
    solar_dict = {}
    for line in csv.reader(solar_data):
        solar_dict[int(line[0])] = line[1]

# GET /universe/structures/
with open(os.path.join(sys.path[0], "Documents\Python Scripts\\NPC_stations.csv"), "r", encoding='utf-8-sig') as npc_data:
    npc_stations_dict = {}
    for line in csv.reader(npc_data):
        npc_stations_dict[int(line[0])] = line[1]
        
# filename4 = "C:/Users/Rollie/Documents/Python Scripts/Problems/EVE Online/player_structures.csv"
# with open(filename4, 'r', encoding='utf-8') as player_data:
#     player_stations_dict = {}
#     for line in csv.reader(player_data):
#         player_stations_dict[int(line[0])] = line[1]


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


# char_info(94881232)

# https://www.adam4eve.eu/info_locations.php
# lonetrek 10000016
# /markets/{region_id}/orders/


def market_orders(region_id):
    
    def make_call(page_no):
        url = 'https://esi.evetech.net/latest/markets/{}/orders/?datasource=tranquility&order_type=all&page={}'.format(region_id, page)
        print("calling page " + str(page))
        response = requests.get(url)
        orders = json.loads(response.content)
        new_df = pd.json_normalize(orders)
        return new_df
    
    page = 1
    df = pd.DataFrame()
    additional = make_call(page)
    df = df.append(additional)
    
    if len(additional) == 1000:
        page +=1
        additional = make_call(page)
        df = df.append(additional)
    
    print(len(df))
    # #pd.set_option('display.max_columns', None)
    # df['type_name'] = df['type_id'].map(id_dict)
    # df['location_name'] = df['location_id'].map(id_dict)
    # df['system_name'] = df['system_id'].map(solar_dict)
    # df['location_name'] = df['location_id'].map(npc_stations_dict)
    # df['price_max'] = df.groupby(['type_name'])['price'].transform(max)
    # df['price_min'] = df.groupby(['type_name'])['price'].transform(min)
    # df = df.is_buy_order == 'true'
    # #df = df[df.price_max != df.price_min]
    # print(df.head(5))
    # #print(df.groupby(['type_name'], sort=False)['price'].max())


    # # для каждого уникального ИД найти минимальный заказ на продажу с минимальной ценой и заказ на  покупку с максимальной ценой и посчитать прибыль
    # # resulting_df = df['type_name'].copy().drop_duplicates()
    # # https://stackoverflow.com/questions/15741759/find-maximum-value-of-a-column-and-return-the-corresponding-row-values-using-pan
    # # print(resulting_df.head(5))

market_orders(10000016)

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


filename = "C:/Users/Rollie/Documents/Python Scripts/Problems/EVE Online/typeids.csv"
with open(filename, 'r', encoding='utf-8') as id_data:
    id_dict = {}
    for line in csv.reader(id_data):
        id_dict[int(line[0])] = line[1]

# GET /universe/systems/
filename2 = "C:/Users/Rollie/Documents/Python Scripts/Problems/EVE Online/solar_systems.csv"
with open(filename2, 'r', encoding='utf-8') as solar_data:
    solar_dict = {}
    for line in csv.reader(solar_data):
        solar_dict[int(line[0])] = line[1]

# GET /universe/structures/
filename3 = "C:/Users/Rollie/Documents/Python Scripts/Problems/EVE Online/NPC_stations.csv"
with open(filename3, 'r', encoding='utf-8') as npc_data:
    npc_stations_dict = {}
    for line in csv.reader(npc_data):
        npc_stations_dict[int(line[0])] = line[1]

filename4 = "C:/Users/Rollie/Documents/Python Scripts/Problems/EVE Online/player_structures.csv"
with open(filename4, 'r', encoding='utf-8') as player_data:
    player_stations_dict = {}
    for line in csv.reader(player_data):
        player_stations_dict[int(line[0])] = line[1]


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
    url = 'https://esi.evetech.net/latest/markets/{}/orders/'.format(region_id)
    response = requests.get(url)
    orders = json.loads(response.content)
    df = pd.json_normalize(orders)
    df['type_name'] = df['type_id'].map(id_dict)
    df['location_name'] = df['location_id'].map(id_dict)
    df['system_name'] = df['system_id'].map(solar_dict)
    df['location_name'] = df['location_id'].map(npc_stations_dict)
    # print(df.head(5))

    # for order in range(len(orders)):
    #     print(orders[order]["order_id"])
    
    # для каждого уникального ИД найти минимальный заказ на продажу с минимальной ценой и заказ на  покупку с максимальной ценой и посчитать прибыль

    # for ware in df.type_id.unique():
    #     print("For ware ID {} min price is {}, max price is {}".format(df[ware],df[price].min(), df[price].max()))

market_orders(10000016)


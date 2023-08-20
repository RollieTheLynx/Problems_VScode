# -*- coding: utf-8 -*-
"""
https://steamcommunity.com/dev
https://partner.steamgames.com/doc/webapi_overview/responses
"""
import json
import requests
import html

def GetNewsForApp():
    appid = 1250410
    count = 3
    maxlength = 300
    url = f'https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={appid}&count={count}&maxlength={maxlength}&format=json'

    get = requests.get(url)
    reply = json.loads(get.content)
    for news in reply['appnews']['newsitems']:
        print(news['title'])
        print(news['contents'], end='\n\n')

GetNewsForApp()


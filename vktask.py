# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie
"""

import json
import requests
#import time
import datetime
#from calendar import timegm
import calendar
from bs4 import BeautifulSoup
import webbrowser
import re

# from_input = input("Введите дату начала периода DD.MM.YYYY: ")
# to_input = input("Введите дату конца периода DD.MM.YYYY: ")
# try:
#     timestamp_from = time.mktime(datetime.datetime.strptime(from_input, "%d.%m.%Y").timetuple())
#     timestamp_to = time.mktime(datetime.datetime.strptime(to_input, "%d.%m.%Y").timetuple())
# except ValueError:
#     print("В формате DD.MM.YYYY, дятел")
    
timestamp_from = 1588291200 # 2020.05.01 unixtime
timestamp_to = 1590883200 # 2020.05.31 unixtime

#%% VK data
# идентификатор приложения, он же API_ID, APP_ID, client_id = 7515392
group_id = 29138817

link = "https://oauth.vk.com/authorize?client_id=7515392&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=stats&response_type=token&v=5.52"
webbrowser.open(link, new=2)

print("В Вашем браузере откроется ВК. Авторизуйтесь и вставьте сюда ссылку")
tok = input("-> ")
    
access_token = re.search(r'token=(.*?)&.', tok).group(1)

#%% лайки и репосты ВК
try:
    vk_stats_request = requests.get(f'https://api.vk.com/method/stats.get?v=5.86&group_id={group_id}&access_token={access_token}&timestamp_from={timestamp_from}&timestamp_to={timestamp_to}&interval=all')

    reply = json.loads(vk_stats_request.content)
except Exception:
    reply = "Не смог подключиться к API stats.get"
#print(reply)

vk_shares=reply["response"][0]["activity"]["copies"]
vk_likes=reply["response"][0]["activity"]["likes"]

#%% число подписчиков VK !на данный момент!
try:
    vk_members = requests.get(f"https://api.vk.com/method/groups.getById?v=5.86&group_id={group_id}&fields=members_count&access_token={access_token}")
    reply2 = json.loads(vk_members.content)
except Exception:
    reply2 = "Не смог подключиться к API groups.getById"

vk_subs = reply2["response"][0]["members_count"]

#%% делаем список id постов за период
try:
    vk_posts = requests.get(f"https://api.vk.com/method/wall.get?v=5.86&owner_id={group_id*-1}&count=50&access_token={access_token}")
    reply3 = json.loads(vk_posts.content)
except Exception:
    reply3 = "Не смог подключиться к API wall.get"

ids = []

for n in range(0,50):
    if reply3["response"]["items"][n]["date"] in range(timestamp_from,timestamp_to+1):
        ids.append(reply3["response"]["items"][n]["id"])
    

vk_comments = 0

for an_id in ids:
    try:
        vk_posts = requests.get(f"https://api.vk.com/method/wall.getComments?v=5.86&owner_id={group_id*-1}&post_id={an_id}&access_token={access_token}")
        reply4 = json.loads(vk_posts.content)
        vk_comments + reply4["response"]["count"]
    except Exception:
        reply4 = "Не смог подключиться к API wall.getComments"

#%%
vk_engagement = (vk_shares + vk_likes + vk_comments) / vk_subs

print("{0:.2%}".format(vk_engagement))

#%% FACEBOOK
'''
To generate an app access token, you need:
    Your App ID
    Your App Secret

Code Sample
curl -X GET "https://graph.facebook.com/oauth/access_token
  ?client_id={your-app-id}
  &client_secret={your-app-secret}
  &grant_type=client_credentials"
  
Permissions

    user_posts
    pages_show_list
    groups_access_member_info
    pages_read_engagement
    pages_read_user_content
    public_profile
'''
fbtoken = "EAAEBGY9Ik8YBAIUE2M9jA7HSAIQ8M49oTBZBc3NAHJxh3mbozpJnxTRoflxUKrLQa14UjynIodnXKWWstvm8CHH1bSfJupZCHUoA4XZAm7W3ZCwl97NbbepQ0cIj4LYuaTmBKRBmX8YuCbGLdPizrQuK2SnNr88N1MjpgHqKwTlVWA6a3eCcYg1W6r2gi0IZD"
fbtest = requests.get(f"https://graph.facebook.com/ProtonElectrotex?fields=posts{{created_time,comments.summary(true),reactions.summary(true),shares.summary(true)}}&access_token={fbtoken}")
fbreply = json.loads(fbtest.content)
fb_comments = 0
fb_reactions = 0
fb_shares = 0
for post in range(0,len(fbreply["posts"]["data"])):
    iso_string = fbreply["posts"]["data"][post]["created_time"]
    # конвертируем дату поста в unixtime
    date_object = datetime.datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%S%z')
    time_stamp = calendar.timegm(date_object.timetuple())
    if time_stamp >= timestamp_from and time_stamp < timestamp_to:
        fb_comments += fbreply["posts"]["data"][0]["comments"]["summary"]["total_count"]
        fb_shares += fbreply["posts"]["data"][0]["shares"]["count"]
        fb_reactions += fbreply["posts"]["data"][0]["reactions"]["summary"]["total_count"]

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get("https://www.facebook.com/ProtonElectrotex/", headers = headers)
#print(response.status_code)
soup = BeautifulSoup(response.content, "html.parser")

company = soup.find("div", {"class": "_4-u2 _6590 _3xaf _4-u8"})
followers_line = company.find("div", {"class": "_4bl9"})
fb_followers = int(followers_line.find("div").get_text().split(" ")[1])

fb_engagement = (fb_shares + fb_reactions + fb_comments) / fb_followers

print("{0:.2%}".format(fb_engagement))


#%% TWITTER

'''Twitter		proto_electro	Lost_prophets_2001'''

import requests, json


account_id = 325653973

req = requests.get(f"https://api.twitter.com/1.1/lists/statuses.json?list_id={account_id}&count=1")
reply = json.loads(req.content)
print(reply)



'''
https://developer.twitter.com/en/docs/basics/authentication/basic-auth

curl -v --compressed -u<email_address>:<password>
    "https://gnip-api.twitter.com/search/30day/accounts/<account-name>/prod/counts.json?query=from%3Atwitterdev"
'''    
ждем ревью

#%% LINKEDIN
# https://docs.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin/context

client_id = "77kqiwkmt748w7"
client_secret = "FrOyDRocQWNpzh1M"


req_token = requests.post(f"https://www.linkedin.com/oauth/v2/accessToken?client_id={client_id}&client_secret={client_secret}")
reply = json.loads(req_token.content)
print(reply)

нет ответа

#%% INSTAGRAM
'''Instagram		protonelectrotex	proton_11_2009'''

app_id = 960496504412918


https://api.instagram.com/oauth/authorize/?client_id=960496504412918&redirect_uri=https://127.0.0.1:8000&response_type=token

# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie

https://api.mangadex.org/docs.html#operation/get-search-manga
"""

# # найти id по тайтлу
# import requests
# title = "Awkward Senpai"
# manga_url = "https://api.mangadex.org/manga"
# parameters = {"title": title}
# r = requests.get(manga_url, params=parameters)
# data = r.json()
# print(data)
# for series in data['results']:
#     print(series["data"]["attributes"]["title"]["en"], end = ": ")
#     print(series["data"]["id"])

# #инфо о манге
# import requests
# manga_id = "a05a7c80-723c-4bba-8cc7-bce8e5116bb1"
# read_url = 'https://api.mangadex.org/manga/{}'.format(manga_id)
# r = requests.get(read_url)
# data = r.json()
# print(data)

# #глава по id
# import requests
# chapter_url = 'https://api.mangadex.org/chapter/52962f45-1fa5-4cae-b53d-e51835855e9d'
# r = requests.get(chapter_url)
# data = r.json()
# print(data)


import requests
import os

title = "Awkward Senpai"
chapter_url = 'https://api.mangadex.org/chapter'
manga_id = "a05a7c80-723c-4bba-8cc7-bce8e5116bb1"
parameters = {"manga": manga_id, 'translatedLanguage': 'en'}
r = requests.get(chapter_url, params=parameters)
data = r.json()
print(data)

chapter_no = 0
for chapter in data["results"]:
    # https://api.mangadex.org/docs.html#section/Chapter-pages-processing/Pages-processing
    data_id = chapter['data']['id']
    server_url = 'https://api.mangadex.org/at-home/server/{}'.format(data_id)
    serv_r = requests.get(server_url)
    serv_reply = serv_r.json()
    base_url = serv_reply['baseUrl']
    chapter_no += 1

    page_no = 0
    for page in chapter["data"]["attributes"]["data"]:
        page_url = "{}/data/{}/{}".format(base_url, chapter["data"]["attributes"]["hash"], page)
        print(page_url)
        download_dir = '{} - {}'.format(title, chapter_no)
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        filepath = f"{os.path.join(os.path.realpath(os.getcwd()), download_dir, str(page_no))}.jpg"
        with open(filepath, "wb") as f:
            f.write(requests.request("GET", page_url).content)
        page_no += 1

# TODO разные расширения
# TODO уже скачанное

# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie

https://api.mangadex.org/docs.html#operation/get-search-manga
"""

import requests
import os

# найти id по тайтлу
def FindID(title):
    manga_url = "https://api.mangadex.org/manga"
    parameters = {"title": title}
    r = requests.get(manga_url, params=parameters)
    data = r.json()
    # предлагаем выданные поиском манги с описанием до переноса строки
    numer = 1
    for series in data['results']:
        print(numer, end = ") ")
        print(series["data"]["attributes"]["title"]["en"], end = ": ")
        print(series["data"]["attributes"]["description"]["en"].split("\r\n")[0])
        numer += 1
    option = input("Which Line is Correct?\n> ")
    return data['results'][int(option)-1]["data"]["id"]

def RequestChaptersBatch(id, offset):
    chapter_url = 'https://api.mangadex.org/chapter'
    parameters = {"manga": id, 'translatedLanguage': 'en', 'offset': offset}
    r = requests.get(chapter_url, params=parameters)
    data = r.json()
    return data

def DownloadChaptersBatch(title, data_batch):
    data = data_batch
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
            extension = page.split(".")[1]
            print('Downloading Chapter {}, page {}'.format(chapter["data"]["attributes"]["chapter"], page_no + 1))
            download_dir = '{} - {}'.format(title, chapter["data"]["attributes"]["chapter"])
            if not os.path.exists(download_dir):
                os.mkdir(download_dir)
            #filepath = f"{os.path.join(os.path.realpath(os.getcwd()), download_dir, str(page_no+1))}.jpg"
            filepath = "{}.{}".format(os.path.join(os.path.realpath(os.getcwd()), download_dir, str(page_no+1)), extension)
            with open(filepath, "wb") as f:
                f.write(requests.request("GET", page_url).content)
            page_no += 1

title = "Abyss"
manga_id = FindID(title)
#manga_id = "a05a7c80-723c-4bba-8cc7-bce8e5116bb1"

# получаем первый батч глав, чтобы узнать общее число глав total и число глав в батче limit
data = RequestChaptersBatch(manga_id, 0)

total_chapters = data["total"]
print(str(total_chapters) + " chapters total")
limit = data["limit"]
# выкачиваем первый батч
DownloadChaptersBatch(title, data)

# выкачиваем все батчи, кроме первого (поэтому начало range с limit)
for batch in range(limit, total_chapters, limit):
    next_data = RequestChaptersBatch(manga_id, batch)
    DownloadChaptersBatch(title, next_data)


#TODO уже скачанное
#TODO название главы
#TODO 0 to cancel
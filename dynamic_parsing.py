# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie

https://www.youtube.com/watch?v=8Uxxu0-dAKQ
"""

# import requests
# '''
# Исследовать элемент, сеть, XHR, GET JSONs
# '''
# url = 'https://unsplash.com/napi/search/photos?query=kitten&per_page=20&page=0&xp='
# r = requests.get(url)
# data = r.json()
# for item in data["results"]:
#     name = item["id"]
#     url = item['urls']["thumb"]
#     print(url)
#     with open(name+'.jpg', "wb") as f:
#         f.write(requests.get(url).content)

import requests
import os


class Unsplash:
    def __init__(self, search_term, per_page=20, quality="thumb"):
        self.search_term = search_term
        self.per_page = per_page
        self.page = 0
        self.quality = quality
        # заголовки с вкладки JSON: https://unsplash.com/napi/search/photos?query=kitten&per_page=20&page=2&xp=
        self.headers = {
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Host': 'unsplash.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
        }

    def set_url(self):
        return 'https://unsplash.com/napi/search/photos?query={}&per_page={}&page={}&xp='.format(self.search_term, self.per_page, self.page)

    def make_request(self):
        url = self.set_url()
        return requests.request("GET", url, headers=self.headers)

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self, name):
        download_dir = "unsplash"
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()), download_dir, name)}.jpg"

    def download(self, url, name):
        filepath = self.save_path(name)
        with open(filepath, "wb") as f:
            f.write(requests.request("GET", url).content)
            #f.write(requests.request("GET", url, headers=self.headers).content)

    def Scraper(self, pages):
        for page in range(0, pages+1):
            self.make_request()
            self.get_data()
            for item in self.data["results"]:
                name = item["id"]
                url = item["urls"][self.quality]
                print(url)
                self.download(url, name)
            self.page += 1


if __name__ == "__main__":
    scraper = Unsplash("kitten")
    scraper.Scraper(1)

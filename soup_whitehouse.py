# -*- coding: utf-8 -*-
"""
Created on Sat May 23 20:32:41 2020

@author: Rollie

https://www.youtube.com/watch?v=87Gx3U0BDlo
"""


import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

#print(result.status_code)
#print(result.headers)

src = result.content

#print(src)

soup = BeautifulSoup(src, "lxml")

urls = []

for a_tag in soup.find_all("a", "news-item__title"):
    print(a_tag.text)
    print(a_tag["href"])

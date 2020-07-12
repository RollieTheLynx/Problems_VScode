# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:11:26 2020

@author: Rollie
"""


import requests
from bs4 import BeautifulSoup

r = requests.get("https://movie.douban.com/subject/30402296/comments")
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all("span", "short")
for item in pattern:
    print(item.string)

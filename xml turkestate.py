# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/xml.etree.elementtree.html#tutorial

"""
import xml.etree.ElementTree as ET
import requests
from datetime import datetime
from os.path import exists
import pandas as pd
from bs4 import BeautifulSoup
import time
import random


current_date = datetime.today().strftime('%Y-%m-%d')


def get_pages():

    if exists(f'turkestate {current_date}.xml'):
        print(f"Today's XML turkestate {current_date}.xml is already downloaded!")
        tree = ET.parse(f'turkestate {current_date}.xml')

    else:
        url = 'https://turk.estate/sitemap.xml'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)

        with open(f'turkestate {current_date}.xml', 'wb') as f:
            f.write(response.content)
        print("Today's XML is downloaded and saved!")

        # You are using xml.etree.ElementTree.parse(), which takes a filename or a file object as an argument.
        # But, you are not passing a file or file object in, you are passing a unicode string.
        # Try xml.etree.ElementTree.fromstring(text):
        tree = ET.fromstring(response.text)

    root = tree.getroot()
    all_pages = tuple((root[child][0].text) for child in range(len(root)))
    return(all_pages)


def fetch(page):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    result = requests.get(page, headers=headers)
    # print(result.status_code)
    # print(result.headers)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    return soup


def parse_page(link):
    soup = fetch(link)

    company = None
    if div_tag := soup.find('div', class_="company center"):  # моржовый оператор := присваивает переменной значение и сразу его возвращает
        if div2_tag := div_tag.find('a'):
            company = div2_tag.text

    name = soup.find('h1', itemprop="name")

    price = None
    if div_tag := soup.find('div', class_="value pointer"):
        if span_tag := div_tag.find('span'):
            price = span_tag.text

    ZhK = None
    if div_tag := soup.find('div', class_="complex"):
        if span_tag := div_tag.find('span', class_="name full"):
            ZhK = span_tag.text

    floor = None
    if div_tag := soup.find('div', class_="floor"):
        if span_tag := div_tag.find('span', class_="value"):
            floor = span_tag.text

    rooms = None
    if div_tag := soup.find('div', class_="rooms"):
        if span_tag := div_tag.find('span', class_="value"):
            rooms = span_tag.text

    area = None
    if div_tag := soup.find('div', class_="square"):
        if span_tag := div_tag.find('span', class_="value"):
            area = span_tag.text

    result = {}
    result['company'] = company
    result['name'] = name.text
    result['price'] = price.replace(u'\xa0', ' ')  # заменяем неразрывный пробел \xa0
    result['complex'] = ZhK
    result['floor'] = floor
    result['rooms'] = rooms
    result['area'] = area

    return result


# test_pages = ['https://turk.estate/real-estate/o50121/o51945/',
#               'https://turk.estate/real-estate/o430/']
# for page in test_pages:
#     result = parse_page(page)
#     print(result)


all_pages = get_pages()
data = []
counter = 1

for link in all_pages:
    if 'real-estate/o' in link and '/q' not in link:  # TODO нужно парсить страницы застройщиков?
        print(f'Parsing object {counter} of {len(all_pages)}: {link}')
        counter += 1
        time.sleep(random.uniform(0.3, 2.9))
        data.append(parse_page(link))

df = pd.DataFrame(data, columns=['company', 'name', 'price', 'complex', 'floor', 'rooms', 'area'])
print(df.head(10))

path = f'turk estate parse {current_date}.xlsx'
with pd.ExcelWriter(path) as writer:
    df.to_excel(writer, sheet_name=f'{current_date}', index=False)

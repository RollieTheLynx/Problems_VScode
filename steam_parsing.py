# -*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=3fcKKZMFbyA
"""

import requests
import csv
import re
from time import sleep
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if not response.ok: # .status_code == 200:
        print(f"Code: {response.status_code}, url: {url}")
    return response.text

def get_games(html):
    soup = BeautifulSoup(html, 'lxml')
    pattern = r'^https://store.steampowered.com/app/'
    games = soup.find_all('a', href=re.compile(pattern))
    print(f'{len(games)} games in total')
    return games

def get_hover_data(id):
    url = f'https://store.steampowered.com/apphoverpublic/{id}'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        title = soup.find('h4', class_ = 'hover_title').text.strip()
    except:
        title = ''
        print(url)
    try:
        released = soup.find('div', class_ = 'hover_release').span.text.split(':')[-1].strip()
    except:
        released = ''
        print(url)
    try:
        reviews_raw = soup.find('div', class_ = 'hover_review_summary').text
    except:
        reviews = ''
        print(url)
    else:
        pattern = r'\d+'
        reviews = int(''.join(re.findall(pattern, reviews_raw)))

    try:
        tags_raw = soup.find_all('div', class_="app_tag")
    except:
        tags = ''
        print(url)
    else:
        tags_text = [tag.text for tag in tags_raw]
        tags = ', '.join(tags_text)

    data = {
        'title': title,
        'released': released,
        'reviews': reviews,
        'tags': tags
    }

    write_csv(data)

def write_csv(data):
    with open('result.csv', 'a', encoding='utf-8') as f:
        fields = ['title', 'reviews', 'released', 'tags']
        writer = csv.DictWriter(f, fieldnames = fields)
        writer.writerow(data)


def main():
    all_games = []
    start = 0
    url = f'https://store.steampowered.com/search/results/?query&start={start}&count=100&tags=1702'

    while True:
        games = get_games(get_html(url))
        if games: # if new batch of games is not empty (=True)
            all_games.extend(games)
            start += 100
            url = f'https://store.steampowered.com/search/results/?query&start={start}&count=100&tags=1702'
        else:
            break

    for game in all_games:
        id = game.get('data-ds-appid')
        get_hover_data(id)

    # https://store.steampowered.com/apphoverpublic/1063730

if __name__ == "__main__":
    main()

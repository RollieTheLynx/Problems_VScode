# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:39:05 2020

@author: Rollie
"""
import requests
from bs4 import BeautifulSoup
import pandas

page = "https://forecast.weather.gov/MapClick.php?x=185&y=107&site=lbf&zmx=&zmy=&map_x=185&map_y=107#.XszCNjlLeUk"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(page, headers = headers)

response.status_code

soup = BeautifulSoup(response.content, "html.parser")

week = soup.find(id = "seven-day-forecast-body")

items = week.find_all(class_ = "tombstone-container")

items[0].find(class_ = "period-name").get_text()
items[0].find(class_ = "short-desc").get_text()
items[0].find(class_ = "temp").get_text()

#list comprehension
period_names = [item.find(class_ = "period-name").get_text() for item in items]
short_descriptions = [item.find(class_ = "short-desc").get_text() for item in items]
temperatures = [item.find(class_ = "temp").get_text() for item in items]

weather_stuff = pandas.DataFrame(
    {"period": period_names,
    "short_descriptions": short_descriptions,
    "temperatures": temperatures
    })

print(weather_stuff)
#weather_stuff.to_excel("weather.xlsx")
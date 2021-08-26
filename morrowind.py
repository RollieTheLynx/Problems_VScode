# -*- coding: utf-8 -*-
"""
https://github.com/hmi-utwente/video-game-text-corpora

"""
import json
with open('imperial_library_20200626b.json') as f:
  data = json.load(f)
games = []

for key in data:
  if data[key]['game'] not in games:
    games.append(data[key]['game'])

print(games)
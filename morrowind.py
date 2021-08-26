# -*- coding: utf-8 -*-
"""
https://github.com/hmi-utwente/video-game-text-corpora

"""
import json
with open('imperial_library_20200626b.json') as f:
    data = json.load(f)

for key in data:
    if "Morrowind" in data[key]["game"]:
        print(data[key]["title"])
        print(data[key]["text"])
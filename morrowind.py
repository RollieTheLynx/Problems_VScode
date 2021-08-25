# -*- coding: utf-8 -*-
"""
https://github.com/hmi-utwente/video-game-text-corpora

"""
import json
with open('imperial_library_20200626b.json') as f:
  data = json.load(f)

print(data["https://www.imperial-library.info/content/dying-mans-last-words"]['text'])
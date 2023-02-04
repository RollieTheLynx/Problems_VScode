# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie
"""

import json
import requests

try:
    api_request = requests.get("https://api.chucknorris.io/jokes/random")
    joke = json.loads(api_request.content)
except Exception:
    joke = "Error..."
print(joke["value"])

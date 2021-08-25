# -*- coding: utf-8 -*-
"""

"""
import json
import requests

qod_url = 'http://jservice.io/api/category'
qod_get = requests.get(qod_url)
qod_reply = json.loads(qod_get.content)
print(qod_reply)
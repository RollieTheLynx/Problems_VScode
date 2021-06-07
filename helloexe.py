# -*- coding: utf-8 -*-

#  pyinstaller helloexe.py

import requests

while True:
    x = input("Press space to download a joke, other key to exit ")
    if x == " ":
        try:
            api_request = requests.get("http://api.icndb.com/jokes/random")
            joke = api_request.json()
        except Exception:
            joke = "Error..."
        print(joke["value"]["joke"])
    else:
        break

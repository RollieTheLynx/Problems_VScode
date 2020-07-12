# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:56:03 2020

@author: Rollie
"""


import requests
r = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
with open('google.png', 'wb') as fp:
     fp.write(r.content)

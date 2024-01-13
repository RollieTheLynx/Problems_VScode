# -*- coding: utf-8 -*-

import requests

s = requests.Session()

userName = {'userName': 'DearJohn'}
location = {'location': 'Tokyo'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookieUrl = 'https://httpbin.org/cookies'

s.get(setCookieUrl, params=userName)
s.get(setCookieUrl, params=location)

r = s.get(getCookieUrl)
print(r.text)

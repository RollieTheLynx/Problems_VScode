# -*- coding: utf-8 -*-
"""

"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.ted.com/talks/eli_pariser_what_obligation_do_social_media_platforms_have_to_the_greater_good'
response = requests.get(url)
soup = BeautifulSoup(response.content, features='lxml')
for script in soup.find_all('script'):
    if (re.search('talkPage.init', str(script))) is not None:
        result = str(script)
result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
mp4_url = result_mp4.split('"')[0]
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
r = requests.get(mp4_url)
with open(file_name, 'wb') as f:
    f.write(r.content)
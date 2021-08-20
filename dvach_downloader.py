# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:34:26 2021

@author: TN90072
"""
import re
import requests
from bs4 import BeautifulSoup

site = 'https://2ch.hk/pr/res/1943168.html'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
a_tags = soup.find_all('a', {"class":"post__image-link"})

urls = [img['href'] for img in a_tags]

for url in urls:
    # url = url.replace('s.', '.')
    # url = url.replace('/thumb/', '/src/')
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|mp4|webm))$', url)
    if not filename:
          print("Regex didn't match with the url: {}".format(url))
          continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the 'site' variable atm. 
            url = '{}{}'.format('https://2ch.hk', url)
        response = requests.get(url)
        f.write(response.content)
        

  
#%% 4chin
site = 'https://boards.4channel.org/an/thread/3700071'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
a_tags = soup.find_all('a', {"class":"fileThumb"})

urls = [img['href'] for img in a_tags]

for url in urls:
    # url = url.replace('s.', '.')
    # url = url.replace('/thumb/', '/src/')
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|mp4|webm))$', url)
    if not filename:
          print("Regex didn't match with the url: {}".format(url))
          continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the 'site' variable atm. 
            url = '{}{}'.format('https:', url)
        response = requests.get(url)
        f.write(response.content)

        
#%% kohl

site = 'https://kohlchan.net/int/res/10976646.html'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
a_tags = soup.find_all('a', {"class":"imgLink"})

urls = [img['href'] for img in a_tags]

for url in urls:
    # url = url.replace('s.', '.')
    # url = url.replace('/thumb/', '/src/')
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|mp4|webm))$', url)
    if not filename:
          print("Regex didn't match with the url: {}".format(url))
          continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the 'site' variable atm. 
            url = '{}{}'.format('https://kohlchan.net', url)
        response = requests.get(url)
        f.write(response.content)

#%% 2ch api

import json
import requests

# https://2ch.hk/abu/res/42375.html

inlink = 'https://2ch.hk/a/res/7160601.html'
board, op_no = inlink.split("/")[3], inlink.split("/")[5].split('.')[0]

thread_url = 'https://2ch.hk/{}/res/{}.json'.format(board, op_no)
thread_get = requests.get(thread_url)
thread_reply = json.loads(thread_get.content)
#print(json.dumps(thread_reply, indent=4, sort_keys=True))

for post_no in range(len(thread_reply['threads'][0]['posts'])):
    for image_no in range(len(thread_reply['threads'][0]['posts'][post_no]['files'])):
        image_link = 'https://2ch.hk/{}'.format(thread_reply['threads'][0]['posts'][post_no]['files'][image_no]['path'])
        file_name = thread_reply['threads'][0]['posts'][post_no]['files'][image_no]['fullname']
        with open(file_name, 'wb') as f:
            image_response = requests.get(image_link)
            f.write(image_response.content)

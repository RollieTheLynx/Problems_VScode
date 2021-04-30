# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie

https://github.com/4chan/4chan-API/blob/master/pages/Endpoints_and_domains.md
"""
import json
import requests
import html

# # print all boards and descriptions
# boards_url = 'https://a.4cdn.org/boards.json'
# boards_get = requests.get(boards_url)
# boards_reply = json.loads(boards_get.content)

# for x in range(len(boards_reply["boards"])):
#     print('{} - {}'.format(boards_reply["boards"][x]["board"], boards_reply["boards"][x]["title"]))

# # print all OP texts in catalof
# board_url = 'https://a.4cdn.org/out/catalog.json'
# board_get = requests.get(board_url)
# board_reply = json.loads(board_get.content)

# for page in range(len(board_reply)):
#     for threads in range(len(board_reply[page]['threads'])):
#         try:
#             print("Page: {}, thread on page: {}, com: {}".format(page, threads, html.unescape(board_reply[page]['threads'][threads]['com'])))
#         except(KeyError):
            # print("Page: {}, thread on page: {}, com: {}".format(page, threads, ""))


thread_url = 'https://a.4cdn.org/out/thread/2084414.json'
thread_get = requests.get(thread_url)
thread_reply = json.loads(thread_get.content)
for post_no in range(len(thread_reply["posts"])):
    try:
        image_link = 'https://i.4cdn.org/out/{}{}'.format(thread_reply["posts"][post_no]["tim"], thread_reply["posts"][post_no]["ext"])
        file_name = '{}{}'.format(thread_reply["posts"][post_no]["filename"], thread_reply["posts"][post_no]["ext"])
        with open(file_name, 'wb') as f:
            image_response = requests.get(image_link)
            f.write(image_response.content)
    except(KeyError):
        continue
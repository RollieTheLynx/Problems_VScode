# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:37:11 2020

@author: Rollie
"""

import vk_api

def two_factor():
    code = input('Code? ')
    return code

vk_session = vk_api.VkApi('lynx_online@mail.ru', 'drtg8h5hw58hTG', auth_handler=two_factor)
vk_session.auth()

vk = vk_session.get_api()

stats = vk.stats.get(group_id=29138817)

print(vk.wall.post(message='Hello world!'))
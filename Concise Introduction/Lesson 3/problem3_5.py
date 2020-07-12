# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:32:17 2020

@author: Rollie
"""


def problem3_5(name):
    """ Looks up the phone number of the person whose name is name """
    
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241", \
                      "james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    if name not in phone_numbers:
        print("No such entry")
    else: print(phone_numbers[name])

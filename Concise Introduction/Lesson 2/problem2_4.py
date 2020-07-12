# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:46:10 2020

@author: Rollie
"""


import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    mylist = []
    count = 0
    while count<10:
        nextitem = random.random()
        mylist.append(nextitem*5+30)
        count = count + 1
    print(mylist)

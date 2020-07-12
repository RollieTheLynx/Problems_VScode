# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:32:20 2020

@author: Rollie
"""


def problem1_3(n):
    my_sum = 0
    current = 1
    while current <= n:
        my_sum = my_sum + current
        current = current + 1
    print(my_sum)
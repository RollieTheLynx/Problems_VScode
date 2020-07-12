# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:47:47 2020

@author: Rollie
"""


def problem2_8(temp_list):
    summa = 0
    for each in temp_list:
        summa = each + summa
        average = summa / len(temp_list)
        maxim = max(temp_list)
        minim = min(temp_list)
    print("Average:",average)
    print("High:",maxim)
    print("Low:",minim)
    
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:29:39 2020

@author: Rollie
"""


def problem3_3(month, day, year):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    output = str(months[month-1]+' '+str(day)+", "+str(year))
    print(output)
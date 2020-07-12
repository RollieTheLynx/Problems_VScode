# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:32:40 2020

@author: Rollie
"""


import csv

def problem3_7(csv_pricefile, flower):
    file = open(csv_pricefile)
    wut = str(flower)
    for row in csv.reader(file):
        if row[0] == wut:
            print(row[1])
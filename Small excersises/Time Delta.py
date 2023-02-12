# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:37:24 2020

@author: Rollie

"""
from datetime import datetime
import time

def calculate():

    date1 = input()
    date1_processed = time.strptime(date1, '%a %d %b %Y %H:%M:%S %z')
    
    hr_diff = int(date1.split()[5][1:3])
    min_diff = int(date1.split()[5][3:5])
    
    if date1.split()[5][0] == "-":
        date1_utc = datetime(date1_processed[0], date1_processed[1], date1_processed[2], date1_processed[3]+hr_diff, date1_processed[4]+min_diff, date1_processed[5])
    elif date1.split()[5][0] == "+":
        date1_utc = datetime(date1_processed[0], date1_processed[1], date1_processed[2], date1_processed[3]-hr_diff, date1_processed[4]-min_diff, date1_processed[5]) 
    
    date2 = input()
    date2_processed = time.strptime(date2, '%a %d %b %Y %H:%M:%S %z')
    
    hr_diff = int(date2.split()[5][1:3])
    min_diff = int(date2.split()[5][3:5])
    
    if date2.split()[5][0] == "-":
        date2_utc = datetime(date2_processed[0], date2_processed[1], date2_processed[2], date2_processed[3]+hr_diff, date2_processed[4] + min_diff, date2_processed[5])
    elif date2.split()[5][0] == "+":
        date2_utc = datetime(date2_processed[0], date2_processed[1], date2_processed[2], date2_processed[3]-hr_diff, date2_processed[4] - min_diff, date2_processed[5])
    
    delta = date1_utc - date2_utc
    
    return int(delta.total_seconds())

n = int(input())

while n > 0:
    difference = calculate()
    print(difference)
    n -= 1
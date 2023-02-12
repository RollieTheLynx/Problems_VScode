# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:58:01 2020

@author: Rollie

https://www.hackerrank.com/challenges/most-commons/problem
"""
s = input()

catalogue = {}
for letter in s:
    if letter not in catalogue:
        catalogue[letter] = 1
    else:
        catalogue[letter] = catalogue[letter] + 1

needed = sorted(catalogue.items(), key=lambda x: (-x[1], x[0]))
print(str(needed[0][0]) + " " + str(needed[0][1]))
print(str(needed[1][0]) + " " + str(needed[1][1]))
print(str(needed[2][0]) + " " + str(needed[2][1]))

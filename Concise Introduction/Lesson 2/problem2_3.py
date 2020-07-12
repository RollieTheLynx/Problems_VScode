# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:45:41 2020

@author: Rollie
"""


newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for state in ne:
        length = len(state)
        print(state,"has",length,"letters.")
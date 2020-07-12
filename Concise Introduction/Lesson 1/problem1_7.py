# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:33:45 2020

@author: Rollie
"""


def problem1_7():
    prebase1 = input("Enter the length of one of the bases: ")
    if prebase1.isdigit():  
        base1 = float(prebase1)
    prebase2 = input("Enter the length of the other base: ")
    if prebase2.isdigit():  
        base2 = float(prebase2)
    preheight = input("Enter the height: ")
    if preheight.isdigit():  
        height = float(preheight)
    print("The area of a trapezoid with bases", base1,"and",base2,"and height",height,"is",1/2*(base1 + base2) * height)

        
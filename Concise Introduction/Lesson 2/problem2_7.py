# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:47:29 2020

@author: Rollie
"""


def problem2_7():
    """ computes area of triangle using Heron's formula. """
    side1=float(input("Enter length of side one: "))
    side2=float(input("Enter length of side two: "))
    side3=float(input("Enter length of side three: "))
    perimieter=(side1+side2+side3)*0.5
    area = perimieter * (perimieter-side1) * (perimieter-side2) * (perimieter-side3)
    print("Area of a triangle with sides",side1,side2,side3,"is",area**0.5)
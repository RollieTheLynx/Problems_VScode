# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:59:59 2020

@author: Rollie

You're writing a program to play a variety of BlackJack. In general, given two numbers, a and b, 
return their sum.

If the sum is greater than 21, return 0, unless one of the numbers is 11. In such a case, the 11 
should be 'converted' to a 1 to prevent the sum from being exceeded.

For example, given a 11 and 13 as input, the 11 should be 'converted' into a 1 so the total sum will be 14. 

"""


a=int(input("a: "))
b=int(input("b: "))

if a+b > 21:
    if a == 11:
        print(1+b)
    if b == 11:
        print(a+1)
    else:
        print(0)
else: print(a+b)
        
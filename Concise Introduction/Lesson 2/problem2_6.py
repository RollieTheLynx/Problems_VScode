# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:47:10 2020

@author: Rollie
"""


import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    count = 0
    while count<100:
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        print(number1+number2)
        count = count+1

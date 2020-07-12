# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:46:52 2020

@author: Rollie
"""


import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    count = 0
    while count<10:
        number = random.randint(1,6)
        print(number)
        count = count+1
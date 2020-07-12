# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:01:23 2020

@author: Rollie
"""


def problem4_1(wordlist):
    """ Takes a word list prints it, sorts it, and prints the sorted list """
    print(wordlist)
    wordlist.sort(key=str.lower)
    print(wordlist)
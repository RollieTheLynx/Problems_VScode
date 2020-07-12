# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:28:54 2020

@author: Rollie
"""


def problem3_1(txtfilename):
    infile = open(txtfilename)
    chars = 0
    for line in infile:
        print(line,end="")
        chars = chars + len(line)
    print()
    print()
    print("There are",chars,"letters in the file.")
    infile.close()
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:27:10 2020

@author: Rollie
"""


import sys     # we need this library to deal with operating system

filename = sys.argv[1]

infile = open(filename)

for line in infile:
    print(line,end="") # the file has "\n" at the end of each line already

infile.close()
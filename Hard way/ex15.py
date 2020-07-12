# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:34:29 2020

@author: Rollie
"""
from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())
def rewind(f):
        f.seek(0)
  
def print_a_line(line_count,f):
    print(line_count, f.readline())
current_file = open(input_file)
print("Whole file:\n")
print_all(current_file)
print("Rewind")
rewind(current_file)
print("Let's print three lines:")
current_line=1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
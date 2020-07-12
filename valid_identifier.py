# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:55:31 2020

@author: Rollie

An identifier in Java, C++ and most other programming languages must begin with a letter and then may be followed by any number of letters or digits.

It is possible that underscores (_) will also appear, but only in the middle and never two consecutively.

Write a program to read a string and output whether it is a valid or invalid identifier. Each string will be 10 characters or less in size.

Example 1:
Enter id: UAB_HSPC
Answer: UAB_HSPC is a valid identifier

Example 2:
Enter id: a_b_c__2
Answer: a_b_c__2 is not a valid identifier
"""
offer = input("Enter ID: ")
mylist = []
for l in offer:
    mylist.append(l)
    
if mylist[0].isalpha() and mylist[0] != "_" and "__" not in offer:
    print(offer,"is a valid identifier")
else: print(offer,"is NOT a valid identifier")
    
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:47:44 2020

@author: Rollie

At UAB football games, Blaze does push ups after each Blazer score. After the first Blazer touchdown (and point after),
Blaze does 7 push ups. After the second touchdown and point after, the score is now 14 and Blaze does 14 push ups.

Write a program that calculates how many total push ups Blaze does during the whole game. Assume that only 7 point touchdowns
(including the point after) occur. Prompt for the final score and print out how many push ups Blaze has done.

Example 1:
Enter final score: 21
Push ups: 42

Example 2:
Enter final score: 7
Push ups: 7
"""

score = int(input("Enter score: "))
total = 0
scores = 0
for i in range(0,score+1,7):
    total = total + scores*7
    scores +=1
print(total,"pushups")
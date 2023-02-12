# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:46:37 2020

@author: Rollie

[['akri', 41.0], ['berry', 37.0], ['har', 39.0], ['harry', 37.0], ['tina', 35.0]]

[['tina', 35.0], ['harry', 37.0], ['berry', 37.0], ['har', 39.0], ['akri', 41.0]]
https://www.hackerrank.com/challenges/nested-list/problem
"""


klass = []
for student in range(int(input())):
    name = input()
    score = float(input())
    new_student = [name, score]
    klass.append(new_student)

sortedKlass = sorted(klass, key = lambda x: float(x[1]))
lowest_score = sortedKlass[0][1]
second_lowest = 0.0

for i in range(student+1):
	   if sortedKlass[i][1] != sortedKlass[0][1]:
	       second_lowest = sortedKlass[i][1]
	       break
                
sec_student_name = [x[0] for x in sortedKlass if x[1] == second_lowest]
sec_student_name.sort()

for s_name in sec_student_name:
    print(s_name)


        

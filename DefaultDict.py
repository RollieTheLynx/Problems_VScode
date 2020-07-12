# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:40:04 2020

@author: Rollie
"""

from collections import defaultdict
   
entry = input()
entry = entry.split(sep = " ")
n = int(entry[0])
m = int(entry[1])
group_A = defaultdict(list)
group_B = defaultdict(list)

#Добавляем в словарь слово и его позицию
for input_n in range(1,n+1):
    group_A[input()].append(input_n)

for input_m in range(1,m+1):
    group_B[input()].append(input_m)
    
for word in group_B: #для каждого слова в группе Б
    if word in group_A:
        for position in range(len(group_A[word])):
            print(group_A[word][position], end=' ')
        print()
    else:
        print(-1)
        
        
        

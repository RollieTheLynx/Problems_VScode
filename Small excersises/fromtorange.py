# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:57:16 2020

@author: TN90072

Генерирует лист чисел xs от start до end  с шагом step, после преобразования добавляет их в лист ys
"""

xs = []
ys = []
start = 0
end = 500
step = 10

while start < end:
    xs.append(start+step)
    start = xs[-1]

for x in xs:
    ys.append(x**2)
    

print(xs[1], ys[1])

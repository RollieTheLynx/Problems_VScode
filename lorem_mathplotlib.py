# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:39:34 2020

@author: TN90072
"""

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

import matplotlib.pyplot as plt

dic = {}

for letter in text:
    if letter not in dic:
        dic[letter.lower()] = 1
    else:
        dic[letter.lower()] += 1

# Построение графика
plt.title("Скока буков") # заголовок
plt.xlabel("Буквы") # ось абсцисс
plt.ylabel("Количество") # ось ординат
plt.grid()      # включение отображение сетки
lists = sorted(dic.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.bar(x, y)
plt.show()
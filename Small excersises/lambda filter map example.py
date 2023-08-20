# -*- coding: utf-8 -*-
"""
Use lambda functions when an anonymous function is required for a short period of time.

"""
x = lambda a : a + 10
print(x(5))


y = lambda a, b : a * b
print(y(5, 6))


z = lambda a, b, c : a + b + c
print(z(5, 6, 2))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


'''
Функция filter() в Python принимает в качестве аргументов функцию и список .
Функция вызывается со всеми элементами в списке, и в результате возвращается новый список,
содержащий элементы, для которых функция результирует в True.
Вот пример использования функции filter() для отбора четных чисел из списка.
'''
my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
filtered_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(filtered_list)


'''
Функция map() принимает в качестве аргументов функцию и список.
Функция вызывается со всеми элементами в списке, и в результате возвращается новый список,
содержащий элементы, возвращенные данной функцией для каждого исходного элемента.
Ниже пример использования функции map() для удвоения всех элементов списка.
'''
current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
mapped_list = list(map(lambda x: x*2 , current_list))
print(mapped_list)
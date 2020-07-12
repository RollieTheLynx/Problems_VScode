# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:47:06 2020

@author: Rollie

Write a program to find the 6-th Monisen number.

Classic Programming Question: find the n-th Monisen number. A number M is a Monisen number if M=2**P-1 and both M and P are prime numbers. 
For example, if P=5, M=2**P-1=31, 5 and 31 are both prime numbers, so 31 is a Monisen number.

Put the 6-th Monisen number into a single text file and submit online.


A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 
Простое число — это натуральное число, больше единицы, имеющее ровно два натуральных делителя: 1 и само себя. 

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, бесконечно.

"""

primes = []

for val in range(2,200000):
    prime = True
    for n in range(2,val):  
        if (val % n) == 0:
            prime = False
    if prime:
        primes.append(val)

monisens = []
    
for P in range(1,200000):
    M = 2**P-1
    if P and M in primes:
        monisens.append(2**P - 1)

print(monisens[5])

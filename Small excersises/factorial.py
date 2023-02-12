# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:50:21 2020

@author: Rollie

If n is an integer greater than 0, n factorial (n!) is the product: n* (n-1) * (n-2) * ( n-3)… *

By convention, 0! = 1.

You must write a program that allows a user to enter an integer between 1 and 7.
Your program must then compute the factorial of the number entered by the user.

Your solution MUST actually perform a computation (i.e., you may not simply print “5040” to the screen as a literal value if the input is 7).

"""
import math
number = int(input("Enter a number: "))
print(number,"! = ",math.factorial(number))

#%%
def recursion(number):
    if number == 1:
        return number
    else:
        return number * recursion(number - 1)

number = int(input("Enter a number: "))
print(number,"! = ",recursion(number))

#%%
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))  
   
#%%
   import sys
  
sys.stdout.write ('Enter a number: ')
  
n = int (input ())
factorial = 1
  
for i in range (1, n + 1) :
    factorial *= i
  
print ('%d! = %d' % (n, factorial))
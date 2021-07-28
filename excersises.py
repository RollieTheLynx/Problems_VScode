# -*- coding: utf-8 -*-
"""
ax^2 + bx + c
quadratic_equation(1, 2, -3) ➞ 1

quadratic_equation(2, -7, 3) ➞ 3

quadratic_equation(1, -12, -28) ➞ 14
"""
def quadratic_equation(a,b,c):
    d = b*2 - 4*a*c
    if d>=0:
        x1 = (-b + d**(1/2))/2*a
        x2 = (-b - d**(1/2))/2*a
    return int(x1)






quadratic_equation(1, 2, -3)

quadratic_equation(2, -7, 3)

quadratic_equation(1, -12, -28)
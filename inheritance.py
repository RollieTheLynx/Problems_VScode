# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:00 2020

@author: Rollie
"""


class Mammal:
    def walk(self):
             print("walk")
             
class Cat(Mammal):
    def meow(self):
        print("meow")

class Nigger(Mammal):
    pass

Tyrone = Nigger()
Tyrone.walk()

Tom = Cat()
Tom.walk()
Tyrone.meow()  #AttributeError: 'Nigger' object has no attribute 'meow'
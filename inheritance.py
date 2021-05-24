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

class Humie(Mammal):
    pass

John = Humie()
John.walk()

Tom = Cat()
Tom.walk()
John.meow()  #AttributeError: 'Humie' object has no attribute 'meow'

# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:01:06 2020

@author: Rollie
"""

#class
class Person:
    #constructor method: this class has these attributes:
    def __init__(self, name, height, weight):
        #attributes
        self.name = name
        self.height = height
        self.weight = weight
    
    #methods
    def talk(self):
        print(f"I am {self.name}. My weight is {self.weight}")
    def kick(self):
        print("kick action")
        
  #Object / instance of class      
John = Person('John',100,10)
John.talk()
John.kick()

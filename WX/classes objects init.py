# -*- coding: utf-8 -*-
"""


https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
"""


class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
#attributes
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

#methods
  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"
    
  #Lets try to create different types of cars  
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)
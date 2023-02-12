# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:08:10 2020

@author: Rollie
"""

from turtle import Turtle, Screen

pg = Screen()
pg.screensize(800, 600)
pg.title("Turtle Race")

car = Turtle("turtle")
current_speed = 1
car.speed(current_speed)
car.color("blue")
car.setposition(0, 250)

# follow = Turtle("turtle")
# follow.speed("fastest")
# follow.color("red")
# follow.penup()
# follow.setposition(-250, -250)

def k1():
    global current_speed
    current_speed += 1

def k2():
    car.left(-5)

def k3():
    car.right(5)

def k4():
    global current_speed
    current_speed -= 1

def quitThis():
    pg.bye()



pg.onkey(k1, "Up")  # the up arrow key
pg.onkey(k2, "Left")  # the left arrow key
pg.onkey(k3, "Right")  # you get it!
pg.onkey(k4, "Down")
pg.onkey(quitThis, 'q')

pg.listen()

car.forward(current_speed)

pg.mainloop()
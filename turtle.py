# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.color("blue")
turtle.left(90)
turtle.speed(7)

def draw (l):
    if l < 1:
        return
    else:
        turtle.forward(l)
        turtle.left(30)
        draw(l/2)
        turtle.right(60)
        draw(l/2)
        turtle.left(30)
        turtle.backward(l)
draw(100)
turtle.mainloop()

#%%

import turtle
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()
turtle.mainloop()

#%%
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(1)

for i in range(6):
    for colours in ["red", "magenta", "blue", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
        
    turtle.hideturtle()

turtle.mainloop()

#%%
from turtle import Turtle, Screen

pg = Screen()
pg.screensize(500, 500)
pg.title("Turtle Keys")

run = Turtle("turtle")
run.speed("fastest")
run.color("blue")
run.penup()
run.setposition(250, 250)

follow = Turtle("turtle")
follow.speed("fastest")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)

def k1():
    run.forward(10)

def k2():
    run.left(45)

def k3():
    run.right(45)

def k4():
    run.backward(10)

def quitThis():
    pg.bye()

def follow_runner():
    follow.setheading(follow.towards(run))
    follow.forward(1)
    pg.ontimer(follow_runner, 10)

pg.onkey(k1, "Up")  # the up arrow key
pg.onkey(k2, "Left")  # the left arrow key
pg.onkey(k3, "Right")  # you get it!
pg.onkey(k4, "Down")
pg.onkey(quitThis, 'q')

pg.listen()

follow_runner()

pg.mainloop()

#%%
import turtle
planet = turtle.Turtle()
planet.speed(1)
planet.color("blue")
planet.setposition(0,-300)

moon = turtle.Turtle()
moon.speed(0)
moon.color("green")
moon.setposition(0,-290)
planet.circle(300)
moon.circle(10)

turtle.mainloop()

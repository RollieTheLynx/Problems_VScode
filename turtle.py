# -*- coding: utf-8 -*-

import turtle

s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("black")
turtle.title("Graphs turtle")

def resetturtle(x,y):
    t.reset()
    t.shapesize(2,2,2)
    t.fillcolor("red")
    t.pensize(1)
    t.pencolor("green")
    t.speed(0)
    t.penup()
    t.hideturtle
    t.setposition(x,y)
    t.pendown()
    t.showturtle
    t.speed(10)

#%%
resetturtle(-450, 0)
xspeed = 1
yspeed = 6
ych = 0.1

for i in range(0,1000):
    t.goto(t.pos()[0] + xspeed, t.pos()[1] + yspeed)
    yspeed += ych
    if yspeed >= 6:
        ych = -0.1
    if yspeed <= -6:
        ych = 0.1
#%%
colors = ["white","pink","green","grey","yellow","red","purple","cyan","magenta", "lime", "salmon", "honeydew", "chocolate", "teal", "maroon", "darkslategray","indigo","deepskyblue"]
resetturtle(0,0)

for color in colors:
    t.pencolor(color)
    t.circle(100)
    t.left (20)
    
#%%
resetturtle(-500, 0)

for x in range(-500,-1):
    y = 500/x
    t.goto(x,y)
    
for x in range(1,500):
    y = 500/x
    t.goto(x,y)
    
#%%

resetturtle(0, 0)  

# turning the turtle to face upwards 
t.rt(-90) 
  
# the acute angle between the base and branch of the Y 
angle = 30
  
# function to plot a Y 
def y(sz, level):    
  
    if level > 0: 
        turtle.colormode(255) 
          
        # splitting the rgb range for green into equal intervals for each level
        # setting the colour according to the current level 
        t.pencolor(0, 255//level, 0) 
          
        # drawing the base 
        t.fd(sz) 
  
        t.rt(angle) 
  
        # recursive call for the right subtree 
        y(0.8 * sz, level-1) 
          
        t.pencolor(0, 255//level, 0) 
          
        t.lt( 2 * angle ) 
  
        # recursive call for the left subtree 
        y(0.8 * sz, level-1) 
          
        t.pencolor(0, 255//level, 0) 
          
        t.rt(angle) 
        t.fd(-sz) 
           
# tree of size 80 and level 7 
y(80, 10) 

#%%
s.mainloop()
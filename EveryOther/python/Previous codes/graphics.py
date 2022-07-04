
from random import *
from turtle import *

colors=["red","blue","green","yellow","purple","orange"]
up ()
goto (-200,0)
down ()
width (5)
hideturtle()
speed (0)
for i in range (9001):
    colorchoice=choice (colors)
    color(colorchoice)
    forward (400)
    right (181)

import turtle
import random
#import math
from random import randint, random
from math import sin, cos, sqrt, pi

pizza = turtle.Turtle()
pizza.speed(0)
pizza.fillcolor('yellow')

pepperoni = turtle.Turtle()
pepperoni.color('red', 'red')

ost = turtle.Turtle()
ost.speed(0)

# Find tilfældig placering inden for cirkel
def placering(x, y, radius):
    r = radius * sqrt(random())
    a = random() * 2 * pi
    x = r * cos(a)
    y = r * sin(a)
    return(x, y)

# Tegn pizza cirkel
def tegn_pizza(x, y, størrelse):
    pizza.penup()
    pizza.goto(x, y - størrelse)
    pizza.begin_fill()
    pizza.pd()
    pizza.stamp()
    pizza.circle(størrelse)
    pizza.end_fill()

def tegn_skinke(antal):
    skinke = turtle.Turtle()
    skinke.speed(0)
    skinke.color('palevioletred')
    for i in range(antal):
        skinke.penup()
        skinke.goto(placering(0, 0, 240))
        skinke.setheading(randint(0, 360))
        skinke.pendown()
        skinke.begin_fill()
        for sider in range(2):
            skinke.fd(25)
            skinke.circle(5, 180)
        skinke.end_fill()

def tegn_ost(x, y, størrelse, farve):
    ost.fillcolor(farve)
    ost.penup()
    ost.goto(x, y)
    ost.begin_fill()
    ost.pendown
    for i in range(5):
        ost.circle(størrelse / 2, 90)
        ost.rt(25)
    ost.end_fill()

def tegn_tomat():
    tomat = turtle.Turtle()
    tomat.color('tomato')
    

#Pepperoni
def tegn_pepperoni(x=0, y=0):
    pepperoni.penup()
    pepperoni.goto(x, y)
    pepperoni.pendown()
    pepperoni.begin_fill()
    pepperoni.circle(50)
    pepperoni.end_fill()

tegn_pizza(0, 0, 250)

tegn_ost(0, -150, 220, 'orange')

tegn_skinke(5)

tegn_pepperoni(80, 50)
tegn_pepperoni(-100, -25)
tegn_pepperoni(-45, 205)
tegn_pepperoni(-200, 175)

turtle.exitonclick()

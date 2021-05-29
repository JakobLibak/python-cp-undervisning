import turtle
from random import randint, random
from math import sin, cos, sqrt, pi, floor

# Find tilfældig placering inden for cirkel
def tilfældig_placering(radius, x=0, y=0):
    r = radius * sqrt(random())
    a = random() * 2 * pi
    x = r * cos(a)
    y = r * sin(a)
    return x, y

# Tegn pizza cirkel
def pizzabund(størrelse, x=0, y=0):
    pizza = turtle.Turtle()
    pizza.speed(0)
    pizza.fillcolor('wheat')

    pizza.penup()
    pizza.goto(x, y - størrelse)
    pizza.begin_fill()
    pizza.pd()
    pizza.circle(størrelse)
    pizza.end_fill()

# Denne funktion spreder skinkestrimler på din pizza
# Angiv størrelse i diameter på pizza og evt. også antal
# tern. Den spreder 50 tern, hvis du kun angiver størrelse.
def skinke(størrelse, antal=50):
    skinke = turtle.Turtle()
    skinke.speed(0)
    skinke.color('palevioletred')
    for i in range(antal):
        skinke.penup()
        skinke.goto(tilfældig_placering(240))
        skinke.setheading(randint(0, 360))
        skinke.pendown()
        skinke.begin_fill()
        for sider in range(2):
            skinke.fd(25)
            skinke.circle(5, 180)
        skinke.end_fill()

# Ost på pizza
def ost(størrelse, x=0, y=0, farve='lightyellow'):
    ost = turtle.Turtle()
    ost.speed(0)

    ost.fillcolor(farve)
    ost.penup()
    ost.goto(x, y)
    ost.begin_fill()
    ost.pendown
    for i in range(5):
        ost.circle(størrelse / 2, 90)
        ost.rt(25)
    ost.end_fill()

def tomat():
    tomat = turtle.Turtle()
    tomat.color('tomato')
    

#Pepperoni
def pepperoni(pizzastørrelse, x=0, y=0, color='firebrick'):
    pepperonistørrelse = floor(pizzastørrelse * 0.1)
    pepperoni = turtle.Turtle()
    pepperoni.color(color, color)

    pepperoni.penup()
    pepperoni.goto(x, y - pepperonistørrelse)
    pepperoni.pendown()
    pepperoni.begin_fill()
    pepperoni.circle(pepperonistørrelse)
    pepperoni.end_fill()
    pepperoni.hideturtle()

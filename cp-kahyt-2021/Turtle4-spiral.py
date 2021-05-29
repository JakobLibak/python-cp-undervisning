# -*- coding: iso-8859-15 -*-
# Python: eks3-1-1.py
# Lad a have 2 og b have 3

import turtle

turtle.setup(width=450,height=450)

skildpadde = turtle.Turtle()
skildpadde.color("green")
skildpadde.pensize(3)

for laengde in range(0, 1000):
    skildpadde.forward(laengde / 100)
    skildpadde.right(3)

turtle.exitonclick()
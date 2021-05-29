# -*- coding: iso-8859-15 -*-
# Python: eks3-1-1.py
# Lad a have 2 og b have 3

import turtle

skildpadde = turtle.Turtle()

turtle.setup(width=450,height=450)
skildpadde.up()
skildpadde.setpos(0,150)
skildpadde.down()
skildpadde.speed(0)

antal_kasser = 24
drej_kasse = 360 / antal_kasser

for kasser in range(0, antal_kasser):
    for side in range(0,4):
        skildpadde.forward(100)
        skildpadde.right(90)
    skildpadde.right(drej_kasse)
    skildpadde.forward(40)


turtle.exitonclick()
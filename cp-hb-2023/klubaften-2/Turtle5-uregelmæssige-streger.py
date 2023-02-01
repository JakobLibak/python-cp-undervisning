# Python: eks3-3-4.py
# Tegn den mange-kant brugeren vil have

import turtle

antal_kanter = int(input("Antal kanter ? "))


turtle.setup(width=450,height=450)

skildpadde = turtle.Turtle()
skildpadde.color("blue")
skildpadde.pensize(2)
skildpadde.penup()
skildpadde.setpos(-100,100)
skildpadde.pendown()

for i in range(0, antal_kanter):
    skildpadde.forward(600/(antal_kanter))
    skildpadde.right(360 / antal_kanter)

turtle.exitonclick()
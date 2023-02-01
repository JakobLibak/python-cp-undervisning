# Python: eks3-1-1.py

# Brug biblioteket turtle (skildpadde)
import turtle

# Lav en skilpadde ved
skildpadde = turtle.Turtle()

# Faa skildpadden til at lave en firkant
# 100 skridt ligenu og drej 90 grader - gentag 4 gange
skildpadde.forward(100)
skildpadde.left(90)

skildpadde.forward(100)
skildpadde.left(90)

skildpadde.forward(100)
skildpadde.left(90)

skildpadde.forward(100)
skildpadde.left(90)

# Vent til paa museklik
turtle.exitonclick()
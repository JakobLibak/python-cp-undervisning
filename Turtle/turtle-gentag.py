import turtle
import random

tegn = turtle.Turtle()

for i in range(0,4):
    tegn.forward(100)
    # tegn.left(90)
    vinkel = randrange(80,100)
    tegn.left(vinkel)

turtle.exitonclick()
import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

t.begin_fill()

for i in range(500):
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.fd(i)
    t.rt(136)
t.end_fill()

turtle.exitonclick()

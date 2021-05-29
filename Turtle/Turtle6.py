import turtle
#from turtle import *
#turtle.color('red', 'yellow')

turtle.bgcolor('orange')

t = turtle.Turtle()

t.pensize(8)
t.color('green', 'blue')
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()

turtle.exitonclick()

import turtle, random


def color(x, y):
    R = random.randrange(0,257,10)
    G = random.randrange(0,257,10)
    B = random.randrange(0,257,10)
    turtle.color(R,G,B)
    turtle.left(10)

turtle.colormode(255)

for i in range(10000):
    turtle.onscreenclick(color)
    turtle.forward(1)

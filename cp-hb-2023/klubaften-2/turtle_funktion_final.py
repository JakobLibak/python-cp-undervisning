import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)

def random_color():
    R = random.randrange(0,256,10)
    G = random.randrange(0,256,10)
    B = random.randrange(0,256,10)

    return(R, G, B)

def tegn(længde, bredde, vinkel, gentagelser, forøgelse=0, penforøgelse=0):
    t.width(bredde)
    for i in range(gentagelser):
        længde += forøgelse
        bredde += penforøgelse

        t.color(random_color())
        t.width(bredde)
        t.fd(længde)
        t.rt(vinkel)

    turtle.exitonclick()
    turtle.resetscreen()

#Stjerne
#tegn(100, 3, 135, 8, 0)

#Firkant
#tegn(100, 5, 90, 4)

#tegn(125, 5, 46, 27)

#tegn(100, 10, 91, 1000, 0.2)


#Trekant
#tegn(1, 5, 120, 3, 1)


#mønster
#tegn(1, 5, 125, 156, 5)


#tegn(100, 5, 135, 500, 5)


#tegn(100, 5, 135, 500, 5, 0.1)

#tegn(2, 4, 1, 30)

#for i in range(t.undobufferentries()):
    #t.undo()


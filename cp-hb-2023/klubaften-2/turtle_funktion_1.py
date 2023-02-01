import turtle

t = turtle.Turtle()
turtle.colormode(255)

def tegn(længde, vinkel, gentagelser):
    for i in range(gentagelser):
        t.fd(længde)
        t.rt(vinkel)

    turtle.exitonclick()
    turtle.resetscreen()

#Firkant
#tegn(100, 90, 4)

#Stjerne
#tegn(100, 135, 8)

#Trekant
#tegn(1, 120, 3)
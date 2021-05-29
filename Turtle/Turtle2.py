import turtle

turtle.setup(width=450,height=300)
skildpadde = turtle.Turtle()

# Tegn vand
skildpadde.up()
skildpadde.setpos(-225, -100)
skildpadde.pensize(12)
skildpadde.color("blue")
skildpadde.down()
skildpadde.forward(450)

# Tegn skib
skildpadde.up()
skildpadde.setpos(-100, -100)
skildpadde.pensize(4)
skildpadde.color("black")
skildpadde.down()

skildpadde.left(90)
skildpadde.forward(30)
skildpadde.right(90)
skildpadde.forward(250)
skildpadde.right(90+45)
skildpadde.forward(45)
skildpadde.right(45)
skildpadde.forward(225)

# Tegn mast
skildpadde.up()
skildpadde.setpos(10, -70)
skildpadde.pensize(4)
skildpadde.color("black")
skildpadde.down()

# Tegn mast
for i in range(0,2):
    skildpadde.right(90)
    skildpadde.forward(200)
    skildpadde.right(90)
    skildpadde.forward(10)

skildpadde.up()
skildpadde.setpos(10, -50)
skildpadde.down()

for i in range(0,2):
    skildpadde.forward(90)
    skildpadde.right(90)
    skildpadde.forward(8)
    skildpadde.right(90)

skildpadde.up()
skildpadde.setpos(10, 130)
skildpadde.pensize(1)
skildpadde.down()
skildpadde.left(62)
skildpadde.forward(200)

turtle.exitonclick()
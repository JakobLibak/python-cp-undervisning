import turtle
#import random
from random import randint

#farver = ['orange', 'blue', 'red']
farver = (randint(0, 255), randint(0, 255), randint(0, 255))

for i in range(102):
    turtle.fd(i)
    turtle.rt(91)
    farve = (randint(0, 255), randint(0, 255), randint(0, 255))
#    print(farve)
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
#    turtle.color(random.choice(farver))

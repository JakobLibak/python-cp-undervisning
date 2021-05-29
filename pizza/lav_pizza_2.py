import turtle
from fyld import pizzabund, skinke, ost, pepperoni
from fyld import tilfældig_placering

pizzastørrelse = 251

# Tegner en pizzabund
pizzabund(pizzastørrelse)


ost(150)
skinke(pizzastørrelse)

for antal in range(2):
    pepperoni(pizzastørrelse, *tilfældig_placering(220))

turtle.exitonclick()

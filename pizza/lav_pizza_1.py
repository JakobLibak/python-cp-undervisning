from fyld import pizzabund, skinke, ost, pepperoni, tilfældig_placering

pizzastørrelse = 250

# Tegner en pizzabund
pizzabund(pizzastørrelse)

# Lægger ost på pizzaen
ost(pizzastørrelse, 50, -150)

# Spreder skinke på pizzaen
skinke(pizzastørrelse)

# Spred pepperonier på hele pizzaen
for skive in range(15):
    pepperoni(pizzastørrelse, *tilfældig_placering(pizzastørrelse - 50))


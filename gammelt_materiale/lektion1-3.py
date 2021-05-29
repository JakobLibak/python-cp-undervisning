# Vi laver en variable som liste og ser forskellen på at printe hele listen
# eller et element ad gangen.

# Her bliver listen deklareret

instructors = 'Jakob', 'Ole', 'Michael', 'Julie', 'Baldur', 'Hlynur'

# Her udskriver vi hele listen
print(instructors)

# Her bruger vi en for løkke til at udskrive et element ad gangen
for navn in instructors:
	print(navn)

# Vi kan også nøjes med at kun udskrive en bestemt position.
# Første position er altid 0
print(instructors[0])


bestillinger = {}

while True:
    navn = input('Hvad hedder du? ')

    if navn == 'stop':
        break
    else:
        ingredienser = []
        while True:
            ingrediens = input('Hvad vil du gerne have på din pizza? ')
            if ingrediens == 'stop':
                break
            else:
                ingredienser.append(ingrediens)
            print(ingredienser)
            bestillinger[navn] = ingredienser

print(bestillinger)

filnavn = 'c:\source\bestillinger.txt'


fil = open(filnavn, 'w+')
for i in bestillinger:
    fil.write(i)

fil.close()

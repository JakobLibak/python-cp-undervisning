
liste = []
inputnavn = 'Navn_98'


for i in range(100):
    ordbog = {'navn': 'Navn_'+str(i)}
    liste.append(ordbog)

# print(liste)

for ordbog in liste:
    # print(ordbog.values())
    # print(ordbog.keys())
    # print('Navn_98' in ordbog.values())
    # print(ordbog['navn'])
    if ordbog['navn'] == inputnavn:
        print('Match!')
        print(ordbog.values())

    if inputnavn in ordbog:
        print('Nyt match!')
personliste = []

for personer in range(10):
    ny_person = {}
    ny_person['navn'] = 'Navn'+str(personer)
    ny_person['egenskab'] = 'Egenskab'+str(personer)
    personliste.append(ny_person)

print(personliste[0])

navne = []

for n in range(len(personliste)):
    print(personliste[n].get('navn'))
    nyt_navn = personliste[n].get('navn')
    navne.append(nyt_navn)

print(navne)

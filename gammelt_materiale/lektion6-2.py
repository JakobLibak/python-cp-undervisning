# Skriv et navn og få et svar tilbage.

navne_jeg_kender = []

while True:
    kendte_antal_navne = len(navne_jeg_kender)

    print('Jeg kender', kendte_antal_navne, 'personer.')
    
    navn = input('Hvad hedder du? ')

    # Sørger for at alle navne bliver stavet med stort begyndelsesbogstav
    navn = navn.title()

    print('Hej', navn)

    if navn in navne_jeg_kender :
        print('Jeg kender dig allerede')
    elif navn == 'Stop':
        break
    else:
        print('Jeg kender dig ikke, men nu tilføjer jeg dig på listen over folk jeg kender.')
        navne_jeg_kender.append(navn)

print('Programmet er afbrudt. Her er de navne jeg kender:')
print(navne_jeg_kender)

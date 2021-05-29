# Lav en ordbog (dictionary) med mulige kombinationer af navne og
# hvad de er (sød, sej, klog, grim, dum, etc.)

personer = {'Jakob': 'sød',
            'Svend': 'fjollet',
            'Niels': 'dum'
            }

# Skriv et navn og få et svar tilbage.

navn = input('Hvad hedder du? ')

# Sørger for at alle navne bliver stavet med stort begyndelsesbogstav
navn = navn.title()

print('Hej', navn)

if navn in personer:
    print("\n", navn, "er", personer[navn])
else:
    print('Jeg kender ikke', navn)


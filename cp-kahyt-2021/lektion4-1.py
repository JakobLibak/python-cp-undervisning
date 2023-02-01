# Skriv et navn og få et svar tilbage.

navn = input('Hvad hedder du? ')

# Sørger for at alle navne bliver stavet med stort begyndelsesbogstav
navn = navn.title()

print('Hej', navn)

if navn == 'Jakob':
    print('Du er sej')
else:
    print('Du er en en landkrabbe!')


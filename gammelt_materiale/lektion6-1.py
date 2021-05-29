# Skriv et navn og få et svar tilbage.

navn = input('Hvad hedder du? ')

# Sørger for at alle navne bliver stavet med stort begyndelsesbogstav
navn = navn.title()

print('Hej', navn)

if navn == 'Jakob':
    print('Du er sej')
elif navn == 'Michael':
    print('Du er en flink fyr')
else:
    print('Jeg kender dig ikke')


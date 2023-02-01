# Lav en ordbog (dictionary) med mulige kombinationer af navne og
# hvad de er (sød, sej, klog, grim, dum, etc.)

# Vi starter denne gang med en tom ordbog
# Programmet kender ingen personer på forhånd.
personer = {}

while True:
    # Skriv et navn og få et svar tilbage.
    navn = input('\nHvad hedder du? ')

    # Sørger for at alle navne bliver stavet med stort begyndelsesbogstav
    navn = navn.title()

    # Hvis navnet er oprettet i personer ordbogen, så sig hej og fortæl hvad
    # vi ved om personen.
    if navn in personer:
        besked  ='Hej ' + navn + '.\n'
        print(besked)
        besked = navn + ' er ' + personer[navn] + '.'
        print(besked)
    # Hvis der bliver skrevet stop, så afbryd while løkken
    elif navn == 'Stop':
        break
    # Ellers fortæl at vi ikke kender navnet endnu, og bed om input.
    else:
        besked = 'Hej ' + navn +'. Jeg kender dig ikke.\nFortæl lidt om dig selv.'
        print(besked)
        spørgsmål = '\nHvad er ' + navn + '? '
        # Gem navn og input i ordbogen, så det er kendt næste gang
        # løkken køres
        personer[navn] = input(spørgsmål)
        # store bogstaver laves om til små her.
        # Ikke strengt nødvendigt, men det ser pænere ud.
        personer[navn] = personer[navn].lower()

# Gå tilbage og start forfra på løkken.

print(personer)



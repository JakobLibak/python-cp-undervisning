# Lektion 4-5
# Vi udvider med at spørge hvornår personen er født og gemmer det som en ekstra
# værdi i ordbogen.

# Lav en ordbog (dictionary) med mulige kombinationer af navne og
# hvad de er (sød, sej, klog, grim, dum, etc.)

# Vi starter denne gang med en tom liste i stedet for en tom ordbog.
# Programmet kender ingen personer på forhånd.
personer = []

while True:
    # Skriv et navn og få et svar tilbage.
    navn = input('\nHvad hedder du? ')

    # Sørger for at alle navne bliver stavet med stort begyndelsesbogstav
    navn = navn.title()
    kendt_person = False

    print(personer)

    # Hvis navnet er oprettet i personer ordbogen,
    # så sig hej og fortæl hvad vi ved om personen.
    for personinfo in personer:
        if personinfo['navn'] == navn:
            kendt_person = True
            kendt_egenskab = personinfo['egenskab']

    # Den her vil også virke:
    # for i in range(len(personer)):
    #     if navn in personer[i]['navn']:
    #         print("Du er genkendt!")

    if kendt_person == True:
        # besked = f'''Hej {navn}.\nDu er {personer[kendt_person_id]['egenskab']}'''
        # print(besked)                
        besked  ='Hej ' + navn + '.\n'
        print(besked)
        besked = 'Du er ' + kendt_egenskab + '.'
        print(besked)
    # Hvis der bliver skrevet stop, så afbryd while løkken
    elif navn == 'Stop':
        break
    # Ellers fortæl at vi ikke kender navnet endnu, og bed om input.
    else:
        besked = 'Hej ' + navn +'. Jeg kender dig ikke.\nFortæl lidt om dig selv.'
        print(besked)
        spørgsmål = '\nHvad er ' + navn + '? '
        egenskab = input(spørgsmål)
        # store bogstaver laves om til små her.
        # Ikke strengt nødvendigt, men det ser pænere ud.
        egenskab = egenskab.lower()

        # ny_person_id = 'Person_' + str(len(personer) + 1)

        ny_person = {'navn': navn,
                    'egenskab': egenskab}
        # Gem navn og input i ordbogen, så det er kendt næste gang
        # løkken køres
        personer.append(ny_person)
        print(f'Tilføjet: {personer[-1]}')

    # try:
    #     for n in range(len(personer)):
    #         nyt_navn = personer[n].get('navn')
    #         navneliste.append(nyt_navn)
    # except:
    #     print('Intet at tilføje')

# Gå tilbage og start forfra på løkken.

print('Jeg kender følgende personer: \n')

for personinfo in personer:
    for info in personinfo:
        besked = f'''
        {info} :  {personinfo[info]}\
        '''
        print(f'{info} :  {personinfo[info]}')
    print('\n')

    # print(personinfo['navn'], 'som er', personinfo['egenskab'])


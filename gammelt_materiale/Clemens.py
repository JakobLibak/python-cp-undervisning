navne_jeg_kender = ["Clemens, Caroline, Sif, Simon, Karen; Bob"]

while True:
    navn = input (" hvad hedder du ? ")

    navn = navn.title()

    print ("hej", navn)

    if navn in navne_jeg_kender :
        print ("jeg kender dig allerede" )
    elif navn == "Stop":
        break
    else:
        print("Jeg kender dig ikke, men  nu tilføjer jeg dig på listen over folk jeg kender.")
        navne_jeg_kender.append(navn)

print ("programet re afbrudt. her er de navne jeg kender:")
print (navne_jeg_kender)

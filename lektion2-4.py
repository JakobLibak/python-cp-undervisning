# https://pythonprogramming.net/functions-learn-python-3-tutorials/?completed=/indexes-slices-learn-python-3-tutorials/
# Vi laver et kryds-og-bolle spil

# I stedet for at udskrive brættet med samme kode hele tiden kan vi lave en funktion der gør det.
# Det svarer til at lave sin egen brik i Scratch.

#Funktionen er defineret her
def spil_bræt():
	print('   0  1  2')
	
	tæller = 0

	for række in spil:
		print(tæller, række)
		tæller += 1

# Det blanke bræt er deklareret her
spil = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

# Vi kalder funktionen nu og udskriver brættet.
spil_bræt()


# Bemærk linjeskift med \n
print('\nVi ændrer position for en brik og udskriver brættet igen.\n')

spil[0][1] = 2

spil_bræt()
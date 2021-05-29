# https://pythonprogramming.net/indexes-slices-learn-python-3-tutorials/?completed=/built-in-functions-learn-python-3-tutorials/
# Vi laver et kryds-og-bolle spil

# Det blanke bræt er deklareret her
spil = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]


print('   0  1  2')

tæller = 0
for række in spil:
	print(tæller, række)
	tæller += 1

# Eller brug nedenstående:
#for tæller, række in enumerate(spil):
#	print(tæller, række)


print('Vi ændrer position for en brik og udskriver brættet igen.\n')

spil[0][1] = 2

print('   0  1  2')

tæller = 0
for række in spil:
	print(tæller, række)
	tæller += 1

# https://pythonprogramming.net/lists-learn-python-3-tutorials/?completed=/tuples-strings-loops-learn-python-3-tutorials/
# Vi laver et kryds-og-bolle spil

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

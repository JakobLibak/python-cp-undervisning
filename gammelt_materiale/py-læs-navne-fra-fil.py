filnavn = 'navne.txt'

with open (filnavn, 'r') as navneinput:
    # lines = navneinput.readlines()

    lines = [line.rstrip() for line in navneinput]

print(lines)
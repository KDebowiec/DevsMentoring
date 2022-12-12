# Odczytaj 4. linię z pliku: test.txt o zawartości:
# line1
# line2
# line3
# line4
# line5
# line6
# line7
plik = open('text.txt', 'r')

lines = plik.readlines()
print(lines[3])

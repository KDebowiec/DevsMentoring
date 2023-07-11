# Napisz program, który sprawdzi, czy string zawiera tylko i wyłącznie zbiór następujących znaków: (a-z, A-Z i 0-9).
import re

plik = open('txt.txt', 'r', encoding='utf8')

txt = plik.read()

if re.search(r"[^a-zA-Z0-9 ]", txt):
    print('zawiera inne')
else:
    print('nie zawiera')

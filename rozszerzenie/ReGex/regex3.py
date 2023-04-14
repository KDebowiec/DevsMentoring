# Sprawdzaj, czy podany string zawiera ciąg dowolnych małych liter rozdzielonych znakiem _, np. aab_cbbbc

import re

plik = open('txt.txt', 'r', encoding='utf8')

txt = plik.read()

if re.search(r"[(\D{1,})\_(\D{1,})]", txt):
    print('zawiera')
else:
    print('nie')
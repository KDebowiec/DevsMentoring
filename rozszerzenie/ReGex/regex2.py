# Sprawdź, czy string rozpoczyna się pojedynczą cyfrą: 0 lub literą ‘b’.
import re


plik = open('txt.txt', 'r', encoding='utf8')

txt = plik.read()

if re.match(r"[b0]", txt):
    print('zaczyna się')
else:
    print('nie zaczyna się')
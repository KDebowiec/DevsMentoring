# Znajdź stringa, który zawiera co najmniej sześć liter i nie zawiera litery ‘A’, np.
#
# unique New York
import re


plik = open('txt.txt', 'r', encoding='utf8')

txt = plik.read()

if re.search(r"[a-z]{6,}", txt):
    print(re.findall(r"[a-z]{6,}[^a]", txt))
else:
    print('nie zawiera')

plik.close()

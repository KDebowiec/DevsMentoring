# Znajdź słowa, które kończą się co najmniej dwiema literami ‘s’, np.
# hiss
# hisssss
# His
import re


plik = open('txt.txt', 'r', encoding='utf8')

txt = plik.read()

if re.search(r"ss$", txt):
    print(re.search(r"[{2,}s]$", txt))
else:
    print('nie zawiera')
# print(re.search(r"[{2,}s]$", txt))
# match = re.search(r"{2,}s$", txt)
# print(match.group())
print(type(txt))
plik.close()

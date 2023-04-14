# Napisz wyrażenie, które sprawdza, czy liczba zmiennoprzecinkowa podana przez użytkownika ma poprawny format.
# Na przykład liczba 123,2341515132135 lub -10 są poprawne, ale 18-12 czy 123, (przecinek na końcu) już nie.
import re


number = (input('wpisz se numerek: '))

if re.match('(-?[0-9]+,?[0-9]?)', number):
    print('git')
else:
    print('nie')
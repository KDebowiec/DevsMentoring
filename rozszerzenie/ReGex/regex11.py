# Sprawdź, czy podany string jest zapisem koloru w systemie szesnastkowym (HEX).
# string musi się zaczynać znakiem #
# następnie musi zawierać 3 lub 6 (ale nie 4 lub 5) znaki kodu szesnastkowego pisane małą lub wielką literą;
#
# Przykłady:
# #ab4
# #AB4B72
#
# Błędne przykłady:
# #ab43
# #aaaaaaaaa
# #ahl
import re

color = input ('wpisz: ')
if re.match('(#[a-zA-Z0-9]{3})', color) or re.match('(#[a-zA-Z0-9]{6})', color):
    print('git')
else:
    print('nie')

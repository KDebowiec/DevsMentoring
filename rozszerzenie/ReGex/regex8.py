# Napisz program, który przyjmować będzie dowolny ciąg znaków oddzielonych spacją.
# Wyodrębnij z niego tylko i wyłącznie te wyrazy, które są liczbami.
#
# Przykładowo dla poniższych danych wejściowych:
# 2 cats and 3 dogs
#
# Zwróć:
# [‘2’, ‘3’]
import re


text = input('wpisz zdanie zawierające cyfry: ')
match = re.findall("[0-9]+", text)
print(match)
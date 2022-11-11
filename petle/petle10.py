# Napisz program, który sprawdzi, czy podana przez usera liczba jest doskonała. Liczba
# doskonała, to taka liczba, która jest sumą wszystkich swoich dzielników właściwych
# (czyli mniejszych od niej samej).
# Przykłady liczb doskonałych: 6 (6 = 1 + 2 + 3), 28, 496, 8128.

divider = 1
sum_of_numbers = 0
number = int(input('czy twoja liczba jest doskonała? podaj by ją sprawdzić: '))
for divider in range(1,number):
    if number % divider == 0:
        sum_of_numbers += divider

if sum_of_numbers == number:
    print('ta liczba jest doskonała')
else:
    print('to nie jest doskonała liczba')
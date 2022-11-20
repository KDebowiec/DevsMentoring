# Napisz skrypt, który wygeneruje i wyprintuje słownik zawierający liczby pomiędzy
# (1 - n; n jest liczbą podawaną przez użytkownika) w formie (x, x*x).
# Przykładowy input: n = 5
# Oczekiwany wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
number = int(input('podaj górną granicę: '))
numbers_dictionary = {}

for number in range(1,number+1):
    numbers_dictionary.update({number : number*number})

print(numbers_dictionary)

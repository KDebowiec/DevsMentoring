# Napisz funkcję, która zwracać będzie “Fizz”, gdy prześlesz do niej wartość podzielną przez 3, “Buzz”,
# gdy podzielną przez 5, a “FizzBuzz”, gdy liczba będzie podzielna przez obie te wartości. Napisz do niej testy jednostkowe.
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'


# Napisz funkcję fizz_buzz, która przyjmuje argument liczbowy.
# 1.  liczba jest podzielna przez 3, funkcja powinna zwrócić “Fizz”.
# 2. Jeżeli liczba jest podzielna przez 5, zwróć “Buzz”.
# 3. Jeżeli liczba jest podzielna równocześnie przez 3 i 5, zwróć “FizzBuzz”.
# 4. W przeciwnym razie, zwracaj przekazaną liczbę.
def fizz_buzz(number):

    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    else:
        print(number)


def main():
    number = int(input('podaj liczbę: '))
    fizz_buzz(number)


if __name__ == '__main__':
    main()
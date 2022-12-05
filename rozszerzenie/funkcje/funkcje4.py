# Napisz funkcję odbierającą w postaci *args dowolną ilość elementów i zwracającą ich iloczyn.

def multiplication(*args):
    number = 0
    for arg in args:
        number += arg
    print(number)


def main():
    number = 1
    while number != 0:
        number = int(input('podaj liczbę, by zakończyć podaj 0: '))
        multiplication()

    multiplication(number)


if __name__ == '__main__':
    main()
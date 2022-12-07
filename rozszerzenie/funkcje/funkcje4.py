# Napisz funkcję odbierającą w postaci *args dowolną ilość elementów i zwracającą ich iloczyn.

def multiplication(*args):
    result = 1

    for number in args:
        result *= number

    print(result)


def main():
    number = 0
    list_of_numbers = []

    while number != 1:
        number = int(input('podaj liczbę, by zakończyć podaj 1: '))
        list_of_numbers.append(number)

    print(list_of_numbers)
    multiplication(*list_of_numbers)


if __name__ == '__main__':
    main()
    # r1 = multiplication(2, 4, 6)
    #
    # print(r1)
    #
    # numbers = [2, 3, 5]
    #
    # r2 = multiplication(numbers)
    #
    # print(r2)

# Napisz funkcję, ktora przyjmować będzie godzinę i minutę (wykorzystaj keyword arguments) i powinna ona zwrócić
# kąt (podany w stopniach) między wskazówką godzinową a minutową w tym podanym czasie.
#
# Podpowiedź:
# Możesz wykorzystać funkcję abs w celu obliczania wartości bezwzględnej, np.
# print(abs(-5)) # 5
# def one_list(**kwargs):
def equation(**kwargs):
    angle = abs(6 * kwargs['kwarg_2'] - 30 * (kwargs['kwarg_1'] + kwargs['kwarg_2'] / 60))
    print(f'kąt między wskazówkami to {angle}')


def main():
    time = input('która jest godzina? podaj w formacie 12:00: ')
    time_list = time.split(':')
    hour = int(time_list[0])
    minute = int(time_list[1])
    equation(kwarg_1=hour, kwarg_2=minute)


if __name__ == '__main__':
    main()




traveled_distance = 100


def set_fuel():
    start_fuel_input = int(input('początkowy poziom paliwa(co najmniej 5000, najwyżej 30000: '))
    while 4999 > start_fuel_input or start_fuel_input > 30000:
        print('podałeś błędną ilość paliwa, spróbuj jeszcze raz')
        start_fuel = int(input('początkowy poziom paliwa(co najmniej 5000, najwyżej 30000: '))
        return start_fuel
    else:
        start_fuel = start_fuel_input
        return start_fuel


def set_astronauts():
    start_astronauts_input = int(input('początkowa liczba astronautów, najwyżej siedmiu: '))
    while 0 >= start_astronauts_input or start_astronauts_input > 7:
        print('podaj właściwą liczbę astronautów!')
        astronauts = int(input('początkowa liczba astronautów, najwyżej siedmiu: '))
        return astronauts
    else:
        astronauts = start_astronauts_input
        return astronauts


reach_ = int((set_fuel() / (300 + 100 * set_astronauts())) * 100)


for i in range(reach_, 0, -100):
    print(f'przebyto {traveled_distance}  km')
    traveled_distance += 100

if traveled_distance >= 2000:
    print('statek dotarł do orbity')
else:
    print('statek nie dotarł do orbity')
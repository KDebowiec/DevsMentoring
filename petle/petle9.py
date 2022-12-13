
traveled_distance = 100

start_fuel = int(input('początkowy poziom paliwa(co najmniej 5000, najwyżej 30000: '))
astronauts = int(input('początkowa liczba astronautów, najwyżej siedmiu: '))

while 5000 > start_fuel or start_fuel > 30000:
    print('podałeś błędną ilość paliwa, spróbuj jeszcze raz')
    start_fuel = int(input('początkowy poziom paliwa(co najmniej 5000, najwyżej 30000: '))

while 0 >= astronauts or astronauts > 7:
    print('podaj właściwą liczbę astronautów!')
    astronauts = int(input('początkowa liczba astronautów, najwyżej siedmiu: '))

reach = int((start_fuel / (300 + 100 * astronauts)) * 100)
usage = 300 + 100 * astronauts

for i in range(reach, 0, -100):
    print(f'przebyto {traveled_distance}  km')
    traveled_distance += 100

if traveled_distance >= 2000:
    print('statek dotarł do orbity')
else:
    print('statek nie dotarł do orbity')
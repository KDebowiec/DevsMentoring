# Pamiętasz zadanie nr 9 z cyklu zadań: 5 Podstawy Pętle (to o astronautach)? Masz następujące zadanie -
# zrefaktoryzować wówczas napisany kod w taki sposób, aby rozwiązanie oprzeć o funkcje!

# Zadeklaruj trzy zmienne - pierwszą przechowującą informację o startowym poziomie paliwa, drugą określającą ilość
# astronautów na pokładzie, a trzecią mówiącą, na jakiej wysokości znajduje się rakieta.
#
# Poproś użytkownika o podanie początkowego poziomu paliwa. Użytkownik ma kontynuować czynność, dopóki nie poda
# poprawnej wartości - mieszczącej się pomiędzy 5000 a 30000 litrów.
# Stwórz drugą pętlę, która będzie prosić o użytkownika o podanie odpowiedniej ilości astronautów znajdujących na
# pokładzie. Pętla ma walidować podaną liczbę - tak, aby była dodatnia i nie większa niż 7.
# Zasymuluj pętlą nr 3 lot statku kosmicznego. Kolejne iteracje mają zmniejszać obecny poziom paliwa o określoną wartość.
# Zużycie paliwa co 100 km zależy od ilości astronautów na pokładzie i jest równe: 300 l + 100 * ilosc_astronautow.
#
# Pętla więc ma uruchamiać się co 100 km i wykonać tyle iteracji, na ile wystarczy paliwa. Co każdą iterację ma
# wyświetlać się aktualnie przebyty dystans przez statek kosmiczny.
#
# Po wykonaniu się pętli, powinien wyświetlić się komunikat: “Statek kosmiczny dotarł do orbity”, jeżeli przebyta
# odległość jest większa niż 2000 km lub w przypadku mniejszej odległości - “Statek kosmiczny nie dotarł do orbity”.
def outputs(reach):
    traveled_distance = 100
    for i in range(reach, 0, -100):
        print(f'przebyto {traveled_distance}  km')
        traveled_distance += 100

    if traveled_distance >= 2000:
        print('statek dotarł do orbity')
    else:
        print('statek nie dotarł do orbity')


def main():
    start_fuel = int(input('początkowy poziom paliwa(co najmniej 5000, najwyżej 30000: '))
    astronauts = int(input('początkowa liczba astronautów, najwyżej siedmiu: '))

    while 5000 > start_fuel or start_fuel > 30000:
        print('podałeś błędną ilość paliwa, spróbuj jeszcze raz')
        start_fuel = int(input('początkowy poziom paliwa(co najmniej 5000, najwyżej 30000: '))

    while 0 >= astronauts or astronauts > 7:
        print('podaj właściwą liczbę astronautów!')
        astronauts = int(input('początkowa liczba astronautów, najwyżej siedmiu: '))

    reach = int((start_fuel / (300 + 100 * astronauts)) * 100)
    outputs(reach)


if __name__ == '__main__':
    main()


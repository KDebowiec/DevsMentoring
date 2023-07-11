list_of_vehicless = []
list_of_depots = []

#zmieniłem class Vehicle od linijki 68(żeby skrócić kod) i def add_bus od linijki 122(żeby użytkownik mógł wybrać
#tylko zajezdnie z listy
class Depot:
    def __init__(self, name):
        self.name = name
        self.list_of_vehicles = []

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

    def add_vehicles_to_depots(self):
        for vehicle in list_of_vehicless:
            if vehicle.depot == self.name:
                self.list_of_vehicles.append(vehicle)

    def return_vehicles(self):
        return self.list_of_vehicles

class TramDepot(Depot):

    def __init__(self, name, kind):
        super().__init__(name)
        self.kind = kind


class BusDepot(Depot):

    def __init__(self, name, kind):
        super().__init__(name)
        self.kind = kind


class Vehicle:

    def __init__(self, max_speed, number, depot):
        self.max_speed = max_speed
        self.number = number
        self.depot = depot

    def __str__(self):
        if hasattr(self, 'wagons'):
            return f" tramwaj nr {self.number}, {self.wagons} wagony, prędkość max: {self.max_speed}, zajezdnia: {self.depot}"
        elif hasattr(self, 'usage'):
            return f" bus nr {self.number}, zużycie {self.usage}, prędkość max: {self.max_speed}, zajezdnia: {self.depot}"

    def __repr__(self):
        return self.__str__()

class Bus(Vehicle):

    def __init__(self, max_speed, number, depot, usage):
        super().__init__(max_speed, number, depot)
        self.usage = usage


class Tram(Vehicle):

    def __init__(self, max_speed, number, depot, wagons):
        super().__init__(max_speed, number, depot)
        self.wagons = wagons


def menu():
    run = True
    while run:
        choice = int(input("jeśli chcesz dodać pojazd, wpisz 1, jeśli chcesz dodać zajezdnie, wpisz 2, jeśli chcesz"
                           "zobaczyć listę pojazdów, wpisz 3, jeśli chcesz zobaczyć pojazdy konkretnej zajezdni, wpisz 4"))
        if choice == 1:
            if list_of_depots:
                bus_or_tram = int(input('żeby dodać bus, wpisz 1, tramwaj wpisz 2: '))
                if bus_or_tram == 1:
                    add_bus()
                elif bus_or_tram == 2:
                    add_tram()
            else:
                print('najpierw dodaj jakąś zajezdnie')
        elif choice == 2:
            what_depot = int(input('zajezdnia busowa, wpisz 1, zajezdnia tramwajowa, wpisz 2: '))
            if what_depot == 1:
                add_bus_depot()
            elif what_depot == 2:
                add_tram_depot()
        elif choice == 3:
            print(list_of_vehicless)
        elif choice == 4:
            show_vehicles()
        elif choice == 5:
            run = False


def add_bus():
    max_speed = int(input('wpisz prędkość maksymalną w km: '))
    number = int(input('wpisz numer pojazdu: '))
    print(list_of_depots)
    depot = input('która zajezdnia: ')
    while depot not in list_of_depots:
        print('wybierz istniejącą zajezdnie')
        depot = input('która zajezdnia: ')
    usage = int(input('podaj zużycie: '))
    new_bus = Bus(max_speed, number, depot, usage)
    list_of_vehicless.append(new_bus)


def add_tram():
    max_speed = int(input('wpisz prędkość maksymalną w km: '))
    number = int(input('wpisz numer pojazdu: '))
    depot = input('która zajezdnia: ')
    wagons = int(input('podaj liczbę wagonów: '))
    new_tram = Tram(max_speed, number, depot, wagons)
    list_of_vehicless.append(new_tram)


def add_bus_depot():
    name = input('podaj nazwę zajezdni autobusowej: ')
    kind = 'zajezdnia autobusowa'
    new_bus_depot = BusDepot(name, kind)
    list_of_depots.append(new_bus_depot)


def add_tram_depot():
    name = input('podaj nazwę zajezdni tramwajowej: ')
    kind = 'zajezdnia tramwajowa'
    new_tram_depot = TramDepot(name, kind)
    list_of_depots.append(new_tram_depot)


def show_vehicles():
    print(list_of_depots)
    choice = input('wybierz zajezdnie')
    print(choice)
    if choice in list_of_depots:
        print(choice.list_of_vehicles)

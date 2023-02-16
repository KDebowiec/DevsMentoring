# Zaprojektuj z użyciem koncepcji dziedziczenia hierarchię klas opisujących pojazdy komunikacji
# miejskiej. Wyraź w tej hierarchii następujące fakty:
#
# 1. wszystkie pojazdy komunikacji miejskiej (k. m.) są pojazdami,
# 2. komunikacja miejska używa tramwajów i autobusów,
# 3. pojazdy są garażowane w zajezdniach, odpowiednio tramwajowych i autobusowych,
# 4. każdy pojazd zna swoją szybkość maksymalną,
# 5. każdy pojazd k. m. zna swój numer,
# 6. każdy pojazd k. m. zna swoją zajezdnię,
# 7. każdy tramwaj jest zestawem 1 do 3 wagonów (i wie, z ilu wagonów się składa),
# 8. każdy autobus wie, ile zużył paliwa w bieżącym miesiącu,
# 9. każda zajezdnia wie, jakie pojazdy do niej należą,
# 10. każda zajezdnia ma nazwę.
#
# Każdy pojazd powinien mieć możliwość podawania swojego opisu w postaci napisu.
# Opis ma zawierać wszystkie informacje, które zna dany pojazd (np. numer, czy szybkość maksymalną).
# Opis zajezdni to nazwa zajezdni, jej typ i opisy poszczególnych pojazdów.
# Zajezdnia autobusowa podaje dodatkowo sumaryczne zużycie paliwa w bieżącym miesiącu,
# a tramwajowa ogólną liczbę wagonów
# Do prezentowania informacji o obiekcie, wykorzystaj metodę specjalną __str__().
#
# Napisz program, który utworzy kilka obiektów reprezentujących wszystkie pojazdy i dwie zajezdnie (autobusową
# i tramwajową), przydzieli pojazdy do zajezdni, a następnie wypisze opis obu zajezdni.

class Depot:

class Vehicle:
    def __init__(self, max_speed, number, depot):
        self.max_speed = max_speed
        self.number = number
        self.depot = depot

    def add_station(self,):

class Bus(Vehicle):
    def __init__(self, max_speed, number, depot, usage):
        super().__init__(max_speed, number, depot)
        self.usage = usage

    def __str__(self):
        return f" bus nr {self.number}, zużycie {self.usage}, prędkość max: {self.max_speed}, zajezdnia: {self.depot}"


class Tram(Vehicle):
    def __init__(self, max_speed, number, depot, wagons):
        super().__init__(max_speed, number, depot)
        self.wagons = wagons

    def __str__(self):
        return f" bus nr {self.number}, {self.wagons} wagony, prędkość max: {self.max_speed}, zajezdnia: {self.depot}"

def add_vehicle(*args):
    created_bus = Bus()
    buses_list.append(created_bus)

def menu():
    if user_input == '1' # wybrał dodanie autobusu
        add_vehicle(user_max_speed ....)
max_speed = input()
bus1 = Bus(max_speed)
# 1) Stwórz klasę Tank (zbiornik).
# Zbiornik posiada następujące atrybuty: nazwę oraz pojemność.
# Należy stworzyć następujące operacje:
# pour_water(volume) - ale w zbiorniku nie może być więcej wody niż pojemność
# pour_out_water(volume) - ale nie można odlać więcej wody niż jest dostępne w zbiorniku
# transfer_water(from, volume) - przelewa wodę ze zbiornika “from” do naszego (pod warunkiem, że przelewanie jest możliwe)
# Dodatkowo stworzyć metody, które pozwalają:
# Znaleźć zbiornik, w którym jest najwięcej wody
# Znaleźć zbiornik, który jest najbardziej zapełniony
# Znaleźć wszystkie puste zbiorniki
# 2) Każda operacja na zbiorniku jest rejestrowana.
# Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik, na którym była ona wykonana
# oraz ilość wody, jaka była brana pod uwagę oraz to, czy operacja się powiodła czy nie.
#
# Należy zaimplementować taką funkcjonalność oraz dodatkowo stworzyć metody, które:
# Pozwalają znaleźć zbiornik, na którym było najwięcej operacji zakończonych niepowodzeniem
# Pozwalają znaleźć zbiornik, w którym było najwięcej operacji danego typu (typ podajemy jako argument metody)
#
# 3) To co zaimplementowaliśmy powyżej to demo “Event Sourcingu” - na czym ono polega?
# Zaimplementuj metodę check_state(tank_name), która pozwoli określić, czy stan wody jest spójny z tym,
# co mamy na liście historii operacji dla danego zbiornika.

EVENT_LOG = []

class Tanks:
    def __init__(self):
        self.tank_dict = {}
        self.menu()


    def menu(self):
        run = True
        while run:
            choice = int(input('co chcesz zrobić? 1 - dodać zbiornik, 2 - nalać wody do zbiornika,'
                               ' 3 - wylać wodę ze zbiornika,'
                               ' 4 - przelać wodę z jednego do drugiego zbiornika, 5 - znaleźć zbiornik z największą \n'
                               'ilością wody, 6 - znależć najbardziej zapełniony zbiornik, 7 - wyszukać wszystkie'
                               'puste zbiorniki, 8 - zatrzymać program: '))

            if choice == 1:
                self.add_tank()
            if choice == 2:
                self.pour_water()
            if choice == 3:
                self.pour_out_water()
            if choice == 4:
                self.transfer_water()
            if choice == 5:
                self.tank_with_most_water()
            if choice == 6:
                self.fullest_tank()
            if choice == 7:
                self.all_empty_tanks()
            if choice == 8:
                run = False

    def add_tank(self):
        name = input('podaj nazwe zbiornika: ')
        capacity = int(input('podaj pojemnośc zbiornika: '))
        volume = int(input('podaj ilość wody w zbiorniku: '))
        new_tank = Tank(name, capacity, volume)
        self.tank_dict.update({name: {'capacity': capacity, 'volume': volume}})
        print(self.tank_dict)
        EVENT_LOG.append({'create': f'Stworzono obiekt {name}'})

    def pour_water(self):
        which_tank = input('do którego zbiornika chcesz dolać wody')
        user_volume = int(input('ile wody chcesz dolać?: '))
        tank_access = self.tank_dict[which_tank]
        if tank_access['capacity'] - tank_access['volume'] >= user_volume:
            tank_access['volume'] += user_volume
        else:
            print('Nie ma miejsca')

        print(self.tank_dict)
    def pour_out_water(self):
        which_tank = input('z którego zbiornika chcesz odlać wody')
        user_volume = int(input('podaj ile wody chcesz wylać: '))
        tank_access = self.tank_dict[which_tank]
        if tank_access['volume'] <= user_volume:
            tank_access['volume'] -= user_volume
        else:
            print('Nie ma tyle wody')
        print(self.tank_dict)

    def transfer_water(self):
        source_tank = input('z którego zbiornika chcesz odlać wody')
        source_tank_access = self.tank_dict[source_tank]
        second_tank = input('do którego zbiornika chcesz nalać wody')
        second_tank_access = self.tank_dict[second_tank]
        user_volume = int(input('podaj ile wody chcesz przelać: '))

        if source_tank_access['volume'] and second_tank_access['capacity'] - second_tank_access['volume'] >= user_volume:
            source_tank_access['volume'] -= user_volume
            second_tank_access['volume'] += user_volume
        else:
            print('nie da się')
        print(self.tank_dict)

    def tank_with_most_water(self):
        tanks_and_vols = {}
        tanks_vols = []

        for name in self.tank_dict:
            tanks_and_vols.update({name: self.tank_dict[name]['volume']})

        for name in self.tank_dict:
            tanks_vols.append(self.tank_dict[name]['volume'])
        max_volume = max(tanks_vols)

        for name in tanks_and_vols:
            if max_volume == tanks_and_vols[name]:
                print(f'{name} ma najwięcej wody')
                return name

        # max_volume = max(tanks_volume)
        # tanks_vols[max_volume]
        # for tank, tank_values in tank_dict.items():
        #     if max_volume == tank_values[volume]:
        #         return tank

    def fullest_tank(self):
        tanks_and_vols = {}
        tanks_vols = []

        for name in self.tank_dict:
            tanks_and_vols.update({name: self.tank_dict[name]['volume'] / self.tank_dict[name]['capacity']})

        for name in self.tank_dict:
            tanks_vols.append(self.tank_dict[name]['volume'] / self.tank_dict[name]['capacity'])
        max_volume = max(tanks_vols)

        for name in tanks_and_vols:
            if max_volume == tanks_and_vols[name]:
                print(f'{name} jest najpełniejszy')
                return name
        try:
            self.record_event('check_full')
        except ValueError:
            print('nic sie nie zrobiło, nie ma eventu')

    def all_empty_tanks(self):
        tanks_and_vols = {}
        empty_tanks = []

        for name in self.tank_dict:
            tanks_and_vols.update({name: self.tank_dict[name]['volume']})

        for name in tanks_and_vols:
            if tanks_and_vols[name] == 0:
                empty_tanks.append(name)

        print(f'zbiorniki {empty_tanks} są puste')
        return empty_tanks

    def record_event(self, event_type):
        EVENT_LOG.append({event_type: text})


class Tank:
    def __init__(self, name, capacity, volume):
        self.name = name
        self.capacity = capacity
        self.volume = volume
        EVENT_LOG.append({'create': f'Stworzono obiekt {self.name}'})


Tanks()

# volume = input('Podaj wode')
# source_tank = tank_list[0]
# target_tank = tank_list[1]
# target_tank.transfer_water(source_tank, volume)

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
from datetime import datetime

EVENT_LOG = [{'zbiornik1': {'time': 12, 'operation_name': 'pour', 'ilość wody': 400, 'succes': True}},
             {'zbiornik1': {'time': 12, 'operation_name': 'pour', 'ilość wody': 400, 'succes': False}}]

class Tanks:
    def __init__(self):
        self.tank_dict = {'zbiornik1': {'capacity': 1000, 'volume': 800},
                          'zbiornik2': {'capacity': 900, 'volume': 300},
                          'zbiornik3': {'capacity': 1100, 'volume': 1100}}
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
            if choice == 9:
                self.show_events()


    def add_tank(self):
        name = input('podaj nazwe zbiornika: ')
        capacity = int(input('podaj pojemnośc zbiornika: '))
        volume = int(input('podaj ilość wody w zbiorniku: '))
        try:
            self.check_volume(volume, capacity)
            new_tank = Tank(name, capacity, volume)
            self.tank_dict.update({name: {'capacity': capacity, 'volume': volume}})
            print(self.tank_dict)
            now = datetime.now()
            EVENT_LOG.append({name: {'time': now, 'operation_name': 'add_tank', 'ilość wody': volume, 'succes': True}})
        except:
            print('wypierdalaj')
            now = datetime.now()
            EVENT_LOG.append({name: {'time': now, 'operation_name': 'add_tank', 'ilość wody': volume, 'succes': False}})

    def check_volume(self, volume, capacity):
        if volume <= capacity:
            pass
        else:
            print('wypierdalaj')
            raise Exception('error')

    def pour_water(self):
        which_tank = input('do którego zbiornika chcesz dolać wody')
        user_volume = int(input('ile wody chcesz dolać?: '))
        tank_access = self.tank_dict[which_tank]
        try:
            self.check_volume(user_volume, tank_access['capacity'] - tank_access['volume'])
            tank_access['volume'] += user_volume
            now = datetime.now()
            EVENT_LOG.append({which_tank: {'time': now, 'operation_name': 'pour_water', 'ilość wody': user_volume, 'succes': True}})
        except:
            print('Nie ma miejsca')
            now = datetime.now()
            EVENT_LOG.append({which_tank: {'time': now, 'operation_name': 'pour_water', 'ilość wody': user_volume, 'succes': False}})
            print(self.tank_dict)

    def pour_out_water(self):
        which_tank = input('z którego zbiornika chcesz odlać wody')
        user_volume = int(input('podaj ile wody chcesz wylać: '))
        tank_access = self.tank_dict[which_tank]
        try:
            self.check_volume(user_volume, tank_access['volume'])
        # if tank_access['volume'] <= user_volume:
            tank_access['volume'] -= user_volume
            now = datetime.now()
            EVENT_LOG.append({which_tank: {'time': now, 'operation_name': 'pour_out_water', 'ilość wody': user_volume, 'succes': True}})
        except:
            print('Nie ma tyle wody')
            print(self.tank_dict)
            now = datetime.now()
            EVENT_LOG.append({which_tank: {'time': now, 'operation_name': 'pour_out_water', 'ilość wody': user_volume, 'succes': False}})

    def transfer_water(self):
        source_tank = input('z którego zbiornika chcesz odlać wody')
        source_tank_access = self.tank_dict[source_tank]
        second_tank = input('do którego zbiornika chcesz nalać wody')
        second_tank_access = self.tank_dict[second_tank]
        user_volume = int(input('podaj ile wody chcesz przelać: '))
        try:
            self.check_volume(user_volume, source_tank_access['volume'])
            self.check_volume(user_volume, second_tank_access['capacity'] - second_tank_access['volume'])
            source_tank_access['volume'] -= user_volume
            second_tank_access['volume'] += user_volume
            now = datetime.now()
            EVENT_LOG.append({source_tank: {'time': now, 'operation_name': 'pour_out_water', 'ilość wody': user_volume, 'succes': True}})
            EVENT_LOG.append({second_tank: {'time': now, 'operation_name': 'pour_water', 'ilość wody': user_volume, 'succes': True}})
        except:
            print('nie da się')
            print(self.tank_dict)
            now = datetime.now()
            EVENT_LOG.append({source_tank: {'time': now, 'operation_name': 'pour_out_water', 'ilość wody': user_volume, 'succes': False}})
            EVENT_LOG.append({second_tank: {'time': now, 'operation_name': 'pour_water', 'ilość wody': user_volume, 'succes': False}})

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

    def show_events(self):
        operation = int(input('jeśli chcesz sprawdzić konkretny zbiornik, wciśnij 1, jeśli chcesz zobaczyć wszystkie udane operacje,'
              'wciśńij 2, jeśli chcesz zobaczyć te nieudane, wciśnij 3: '))
        if operation == 1:
            choice = input('który zbiornik chcesz sprawdzić: ')
            for dict_ in EVENT_LOG:
                if choice in dict_:
                    if dict_[choice]["operation_name"] == 'pour':
                        print('typ operacji: dolewanie wody do zbiornika')
                    elif dict_[choice]["operation_name"] == 'pour_out_water':
                        print('odlewanie wody ze zbiornika')
                    elif dict_[choice]["operation_name"] == 'add_tank':
                        print('dodawanie zbiornika')
                    print(f'data i czas: {dict_[choice]["time"]}, '
                          f'ilość wody: {dict_[choice]["ilość wody"]}, ')
                    if dict_[choice]["succes"]:
                        print('operacja zakończona sukcesem')
                    else:
                        print('operacja nieudana')
        elif operation == 2:
            for dict_ in EVENT_LOG:
                for i in dict_:
                    if dict_[i]['succes']:
                        f'dict_[i][]'



class Tank:
    def __init__(self, name, capacity, volume):
        self.name = name
        self.capacity = capacity
        self.volume = volume


Tanks()



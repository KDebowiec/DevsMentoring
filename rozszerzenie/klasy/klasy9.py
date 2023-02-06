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
class Tank:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def pour_water(self, volume):
        pass

    def pour_out_water(self, volume):
        pass

    def transfer_water(self, from_, volume):
        pass

    def tank_with_most_water(self):
        pass

    def fullest_tank(self):
        pass

    def all_empty_tanks(self):
        pass
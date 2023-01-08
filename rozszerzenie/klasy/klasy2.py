# Stwórz klasę reprezentującą pojazd. Dodaj do niej pola określające maksymalną prędkość obiektu oraz jego przebieg.
# Dodaj do klasy metodę, która zwiększać będzie wartość pola przebiegu o przesłaną wartość typu float.
class Car:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_mileage(self):
        increase = int(input('podaj o ile zwiększył się przebieg: '))
        self.mileage += increase
        print(f'obecnie przebieg to {self.mileage}')


new_car = Car("toyota", 210, 200000)
new_car.increase_mileage()
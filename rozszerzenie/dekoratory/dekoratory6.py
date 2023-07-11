# Zapoznaj się, do czego służą wbudowane w standard Pythona poniższe dekoratory: @property,
# @dataclass, @classmethod i @staticmethod.
# Zbuduj proste programy przedstawiające realizację tych dekoratorów i różnice między nimi.

# -------    @property    -----------
class CodeCouple(object):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == 'Agnieszka':
            self.__name = 'beautiful'
        elif name == 'Krzysztof':
            self.__name = 'ugly'
        else:
            self.__name = 'CodeCouple'


agnieszka = CodeCouple('Agnieszka')
print(agnieszka.name)

krzysztof = CodeCouple('Krzysztof')
print(krzysztof.name)

code_couple = CodeCouple('UglyKrzysztof')
print(code_couple.name)

# -------    @dataclass    -----------
import dataclasses


@dataclasses.dataclass()
class Vehicle:
    wheels: int
    electric: bool
    name: str

    def __str__(self):
        if self.electric:
            return f'{self.name} ma {self.wheels} koła i jest elektryczny'
        else:
            return f'{self.name} ma {self.wheels} koła i nie jest elektryczny'


print(Vehicle(4, True, 'Fiat'))


# -------    @classmethod    -----------
class ClassMethod:

    # def __init__(self, func):
    #     self.func = func
    #
    # def __get__(self, instance, owner):
    #     return self.func.__get__(owner, type(owner))
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def __str__(self):
        return f'Brand: {self.brand} Model: {self.model} Speed: {self.speed}'

    def is_fast(self):
        return self.speed > 200

    @classmethod
    def porsche(cls):
        return cls('Porsche', '911', 300)

    @classmethod
    def different_constructor(cls, brand, model):
        return cls(brand, model, 400)

    # -------    @staticmethod    -----------

    # class StaticMethod:
    #     def __init__(self, func):
    #         self.func = func
    #
    #     def __get__(self, instance, owner):
    #         return self.func
    #
    #     def __call__(self, *args, **kwargs):
    #         return self.func(*args, **kwargs)
    @staticmethod
    def find_fastest_car(cars):
        return max(cars, key=lambda car: car.speed)


print(Car.porsche())

print(Car.different_constructor('BMW', 'X5'))

cars = [Car.porsche()]
print(Car.find_fastest_car(cars))

# Stwórz klasę reprezentującą studenta. Cechy studenta określaj z poziomu konstruktora.
# Dodaj do klasy metodę wyświetlającą informacje o danym obiekcie.
class Student:
    def __init__(self, name, age, university, field):
        self.name = name
        self.age = age
        self.university = university
        self.field = field

    def print_info(self):
        print(f'student {self.name} ma {self.age} lata i  studiuje {self.field} na {self.university}')


karol = Student("Karol", 4, "AGH", "Automatyka")
print(karol.print_info())

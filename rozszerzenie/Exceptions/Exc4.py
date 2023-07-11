#Napisz program, który poprosi użytkownika o wprowadzenie swojego imienia i nazwiska
#oraz wieku. Następnie program ma utworzyć obiekt klasy Osoba, który przechowuje imię, nazwisko i wiek użytkownika.
#Jeśli podany wiek jest mniejszy niż 0 lub większy niż 120, program powinien wygenerować własny wyjątek NiepoprawnyWiekError
#i wyświetlić odpowiedni komunikat użytkownikowi.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class IncorrectAgeError(Exception):
    pass


try:
    name = input('podaj imie: ')
    surname = input('podaj nazwisko: ')
    age = int(input('Podaj wiek: '))
    if age not in range(0, 121):
        raise IncorrectAgeError('Niepoprawny wiek')
    person = Person(name, surname, age)
except IncorrectAgeError as e:
    print(e)

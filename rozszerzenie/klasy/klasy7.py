# Utworzyć klasy Notatka (Note) i Notatnik (Notebook). Klas notatki przechowuje autora, treść i czas utworzenia
# (autor i treść są podawane jako argumenty konstruktora, a czas jest pobierany i zapisywany przy tworzeniu obiektu).
# Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów, lecz tworzy pustą listę do której będą dodawane obiekty
# klasy Notatka. Klasa Notatnika musi posiadać implementacje metod, pozwalających: dodać nową notatkę, dodać istniejącą
# notatkę, sprawdzić ile jest dodanych notatek, wyświetlić wszystkie dodane notatki.
# Dodatkowo musi być obsłużona sytuacja kiedy notatnik jest pusty.
# Podpowiedź:
# do reprezentacji czasu można użyć modułu
# datetime
# Dokumentacja modułu
# datetime
# https://docs.python.org/3/library/datetime.html
import datetime


class Notebook:
    def __init__(self):
        self.notes = []

    def menu(self):
        run = True
        while run:
            choice = int(input('co chcesz zrobić? 1 - dodać notatkę, 2 - usunąć notatkę, 3 - sprawdzić liczbę notatek,'
                               ' 4 - wyświetlić wszystkie notatki, 5 - zakończyć program: '))
        if choice == 1:

        elif choice == 2:

        elif choice == 3:

        elif choice == 4:

        elif choice == 5:
            run = False



class Note:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.time = datetime.datetime.now()

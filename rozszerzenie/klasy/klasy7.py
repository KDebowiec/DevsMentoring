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
        self.menu()

    def menu(self):
        run = True
        while run:
            choice = int(input('co chcesz zrobić? 1 - dodać notatkę, 2 - usunąć notatkę, 3 - sprawdzić liczbę notatek,'
                               ' 4 - wyświetlić wszystkie notatki, 5 - zakończyć program: '))

            if choice == 1:
                self.add_note()
            if choice == 2:
                self.delete_note()
            if choice == 3:
                self.check_length()
            if choice == 4:
                self.show_notes()
            if choice == 5:
                run = False

    def add_note(self):
        author = input('kto jest autorem: ')
        content = input('treść: ')
        note_id = 1
        for i in self.notes:
            note_id += 1
        new_note = Note(author, content, note_id)
        self.notes.append(new_note)

    def delete_note(self):
        if len(self.notes):
            print(self.notes)
            which = int(input('którą notatkę chcesz usunąć, podaj id: '))
            element = self.notes[which+1] #To nie tak ma być
            index_to_delete = self.notes.index(element)
            self.notes.pop(index_to_delete)

    def check_length(self):
        print(f'liczba notatek: {len(self.notes)}')

    def show_notes(self):
        print('Twoje notatki: ')
        for i in self.notes:
            print(i)


class Note:
    def __init__(self, author, content, note_id):
        self.author = author
        self.content = content
        self.time = datetime.datetime.now()
        self.note_id = note_id

    def __repr__(self):
        return f'{self.author}: {self.content}, {self.time}, id notatki: {self.note_id}'


Notebook()
# Napisz program, który będzie wyświetlał Menu z następującymi opcjami:
#
# Dodaj notatkę
# Dodaj wizytówkę (Card)
# Wyświetl wszystkie notatki
# Wyświetl wszystkie wizytówki
# Wyjdź
#
#
# Program ma być podzielony na następujące klasy: Manager (który zawierać będzie komponent:
# Menu, NotesSubManager, CardsSubManager).
#
# Metody w Manager:
# start - metoda wywoływana jako pierwsza z poziomu main
# show_menu (wtedy metoda odwołuje się do obiektu Menu i wywołuje z niej odpowiednią metodą wyświetlającą Menu)
# execute (metoda pobierająca od użytkownika wybór i wywołująca odpowiednią metodę z NotesSubManager/CardSubManager)
# show_notes/show_cards (wywołujące metodę show z odpowiedniego SubManagera)
#
# Metody w Menu:
# show (wyświetlanie menu)
# get_choice (pobieranie wyboru z menu od użytkownika)
#
# Pola w SubManagerach:
# lista na obiekty reprezentujące dodane Notatki/Wizytówki
#
# Metody w SubManagerach:
# add (dodawanie odpowiednio notatki lub karty)
# show (wyświetlanie wszystkich notatek lub kart z listy)


# klasy: Manager, #SubManager, Menu, #SubMenu, Card, Note

# Manager -> Menu
#    1. SubManager_1 -> Menu (add_card, show_list)
#    2. SubManager_2 -> Menu (add_card, show_list)
#    3. Exit
#
#class Card:
#    def __init__(self):
#        self.list_of_cards = []
#
#    def add_card(self):
#        card = input('wpisz wizytówkę: ')
#        self.list_of_cards.append(card)
#
#
#class Note:
#    def __init__(self):
#        self.list_of_notes = []
#
#

class Menu:
    def __init__(self, **kwargs):
        for menu_choice, menu_item in kwargs.items():
            setattr(self, menu_choice, menu_item)
        self.show()
        self.get_choice()

    def show(self):
        for menu_choice, menu_item in self.__dict__.items():
            print(menu_choice, menu_item)

    def get_choice(self):
        user_input = input('Wybierz numer:')
        print(f'Wybrałeś {user_input} czyli {getattr(self, user_input)}')
        self.execute(int(user_input))


class Manager(Menu):
    def __init__(self, menu):
        super().__init__(**menu)

    def execute(self, choice):
        if choice == 1:
            NoteManager(note_menu)

class NoteManager(Manager):
    def __init__(self, menu):
        self.list_of_notes = []
        super().__init__(menu)

    def add_note(self):
        note = input('Wpisz notatkę: ')
        self.list_of_notes.append(note)

    def execute(self, choice):
        if choice == 1:
            self.add_note()

note_menu = {'1': 'Dodaj notatkę', '2': 'Wyświetl wszystko'}
tmp_menu = {'1': 'Manager notatek'}
Manager(tmp_menu)

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

class Manager:

    def start(self):
        pass
        #metoda wywoływana jako pierwsza z poziomu main, chuj wie

    def show_menu(self):
        pass
        # odwołanie do klasy menu i wywołanie metody show


class Menu:

    def show(self):
        print('1. Dodaj notatkę')
        print('2. Dodaj Wizytówkę')
        print('3. Wyświetl notatki')
        print('4. Wyświetl Wizytówki')
        print('5. Wyjdź')

    def get_choice(self):
        choice = int(input())
        return choice


class Card:
    def __init__(self):
        self.list_of_cards = []

    def add_card(self):
        pass


class Note:
    def __init__(self):
        self.list_of_notes = []

    def add_note(self):
        pass

Manager.start()
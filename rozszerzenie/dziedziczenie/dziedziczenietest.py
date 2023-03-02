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
        if choice == 2:
            CardManager(card_menu)
        if choice == 3:
            exit()


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
        if choice == 2:
            for i in self.list_of_notes:
                print(i)


class CardManager(Manager):
    def __init__(self, menu):
        self.list_of_cards = []
        super().__init__(menu)

    def add_card(self):
        card = input('Wpisz wizytówkę: ')
        self.list_of_cards.append(card)

    def execute(self, choice):
        if choice == 1:
            self.add_card()
        if choice == 2:
            for i in self.list_of_cards:
                print(i)


note_menu = {'1': 'Dodaj notatkę', '2': 'Wyświetl wszystko'}
card_menu = {'1': 'Dodaj wizytówkę', '2': 'Wyświetl wszystko'}
tmp_menu = {'1': 'Manager notatek', '2': 'Manager Wizytówek', '3': 'Wyjdź'}
Manager(tmp_menu)

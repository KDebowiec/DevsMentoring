# Zakładasz sklep, w którym będziesz sprzedawał trzy kategorie (Category)
# produktów (ShopItem):
# - ciuchy
# - suplementy
# - buty
# Każdy produkt rozpoznawany jest po nazwie i rozmiarze (ciuchy i suplementy
# mają rozmiary S → XXL, buty 37→ 51).
# Jako pracownik sklepu (ShopWorker) musisz wprowadzić produkty do bazy sklepu
# (ShopDataBase).
# W bazie możesz dodawać, usuwać oraz przeglądać produkty.
# Jeżeli już wprowadzono dany produkt z nazwą i rozmiarem, baza sklepu ma o tym
# poinformować i pominąć dodawanie.
# Do pomocy zatrudniłeś drugiego pracownika, ale może on tylko dodawać produkty i
# je przeglądać, ponieważ nie jest właścicielem.
# Model ShopDataBase potraktuj jako menu który będzie miał akcje:
# - zaloguj lub wyloguj (info kto jest obecnie zalogowany)
# - lista produktów
# - dodaj produkt
# - usuń produkt

class ShopItem:

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Category(ShopItem):
    def __init__(self, name, size):
        super.__init__(name, size)
        self.list_of_
    def __str__(self):
        return f'nazwa: {self.name}, rozmiar: {self.size}'

    def __repr__(self):
        return self.__str__()


class Menu:
    def __init__(self, **kwargs):
        for menu_choice, menu_item in kwargs.items():
            setattr(self, menu_choice, menu_item)
        self.show()
        self.get_choice()

    def show(self):
        for menu_choice, menu_item in self.__dict__.items():
            print(menu_choice, menu_item)
        self.get_choice()

    def get_choice(self):
        user_input = input('Wybierz: ')
        print(f'Wybrałeś {user_input} ')
        self.execute(int(user_input))


class Manager(Menu):

    def __init__(self, menu, user=None, managers_dict={}):
        self.user = user
        self.manager_list = managers_dict
        self.manager_list[self.__class__.__name__] = self
        super().__init__(**menu)

    def execute(self, choice):
        if choice == 1:
            if user == 'Admin':
                ShopDataBase(admin_menu)
            else:
                ShopDataBase(user_menu)


class ShopDataBase(Manager):
    def __init__(self, menu):
        self.products = {}
        user = input('Jesteś admin?')
        super().__init__(menu, user)

    def add_product(self):
        name = input('podaj nazwę: ')
        size = input('wybierz rozmiar S, L, Xl, XXl: ')
        types = input('wybierz typ: ciuchy, suplementy, buty: ')
        new_product = ShopItem(name, size, types)
        id_ = id(new_product)
        self.products.update({id_: {'nazwa': name, 'rozmiar': size, 'typ': types}})
        self.show()

    def delete_product(self):
        chosen = int(input('podaj id produktu który chcesz usunąć: '))
        self.products.pop(chosen)
        self.show()

    def print_products(self):
        for i in self.products.items():
            print(i)

    def execute(self, choice):
        if choice == 1:
            self.print_products()
            self.show()
        if choice == 2:
            self.add_product()
            self.show()
        if choice == 3:
            self.user = None
            self.manager_list['Manager'].show()
        if choice == 4:
            if self.user == 'Admin':
                self.delete_product()
                self.show()
            else:
                print('nie masz takich uprawnień')

#owner = ShopWorker(owner=True, first_name='Karol')
#worker = ShopWorker(owner=False, first_name='Paweł')

admin_menu = {'1': 'Lista produktów', '2': 'dodaj produkt', '3': 'wyloguj', '4': 'usuń produkt'}
user_menu = {'1': 'Lista produktów', '2': 'dodaj produkt', '3': 'wyloguj'}
not_logged_menu = {'1': 'zaloguj'}

user = input('podaj login: ')
Manager(not_logged_menu, user)


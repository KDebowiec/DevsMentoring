
class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def choose_category(self):
        pass


class ShopItem(Category):
    def __init__(self, category_name, name, size):
        super().__init__(category_name)
        self.name = name
        self.size = size


class ShopWorker:
    def __init__(self, owner, first_name):
        self.owner = owner
        self.first_name = first_name


class ShopDataBase:
    def __init__(self):
        self.products = {}
        self.clothes_sizes = ['S', 'M', 'L', 'XL', 'XXL']
        self.shoes_sizes = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
        self.user = None
        self.show()

    def log_in(self):
        self.user = input('login: kim jesteś? ')
        self.show()

    def log_out(self):
        self.user = None
        print('wylogowałeś się!!!!!! ')
        self.show()
        return self.user

    def show(self):
        choice_from_menu = int(input('1: Lista produktów\n2: dodaj produkt\n3: zaloguj/wyloguj\n4: usuń produkt\nwybór: '))
        if choice_from_menu == 1:
            self.print_products()
        elif choice_from_menu == 2:
            self.add_product()
        elif choice_from_menu == 3:
            if self.user:
                self.log_out()
            else:
                self.log_in()
        elif choice_from_menu == 4:
            self.delete_product()

    def add_product(self):
        type_choice = int(input('typ produktu:\n1 - ciuchy\n2 - suplementy\n3 - buty\nwybierz: '))
        if type_choice == 1:
            category_name = 'ciuchy'
            size = input('wybierz rozmiar S, M, L, Xl, XXl: ')
            if size not in self.clothes_sizes:
                print('Nie ma takiego rozmiaru typie')
        elif type_choice == 2:
            category_name = 'suplementy'
            size = int(input('wybierz rozmiar od 37 do 51: '))
            if size not in self.shoes_sizes:
                print('Nie ma takiego rozmiaru typie')
        elif type_choice == 3:
            category_name = 'buty'
            size = input('wybierz rozmiar S, M, L, Xl, XXl: ')
            if size not in self.clothes_sizes:
                print('Nie ma takiego rozmiaru typie')
        name = input('podaj nazwę: ')
        new_product = ShopItem(name, size, category_name)
        id_ = id(new_product)
        self.products.update({id_: {'nazwa': name, 'rozmiar': size, 'typ': category_name}})
        self.show()

    def delete_product(self):
        if self.user == owner.first_name:
            self.print_products()
            chosen = int(input('podaj id produktu który chcesz usunąć: '))
            self.products.pop(chosen)
            self.show()
        else:
            print('nie masz uprawnień!')
            self.show()

    def print_products(self):
        for i in self.products.items():
            print(i)
        self.show()


owner = ShopWorker(owner=True, first_name='Karol')
worker = ShopWorker(owner=False, first_name='Paweł')


ShopDataBase()

class Category:

    def __init__(self, category_name):
        self.category_name = category_name

    def __str__(self):
        return self.category_name

    def get_sizes(self):
        if self.category_name.lower() == 'buty':
            return [size for size in range(37, 51)]
        return ['XS', 'S', 'M', 'L', 'XL', 'XXL']


class ShopItem(Category):

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{ self.name } - { self.size } { (self.category_name) }'


class ShopWorker:

    def __init__(self, login, owner=False):
        self.login = login
        self.owner = owner

    def __str__(self):
        return self.login

    def __repr__(self):
        return self.__str__()


class ShopDataBase:

    def __init__(self, users, categories, logged_in_user=None, products={}):
        self.users = users
        self.logged_in_user = logged_in_user
        self.products = products
        self.categories = categories
        self.show_menu()

    def show_menu(self):
        # Domyślne menu
        menu = {
            '1': 'Lista produktów',
            '2': 'Zaloguj',
        }
        if self.logged_in_user:
            # Sprawdzenie czy ta wartość nie jest None
            # Jeżeli ktoś się zalogował to na pewno to pracownik sklepu i może dodawać produkty i wylogować się
            menu['2'] = 'Dodaj produkt'
            menu['3'] = 'Wyloguj się'
            if self.logged_in_user.owner:
                # Jeżeli to owner to dodajemy do menu akcję usuwania produktu
                # owner może być tylko True lub False
                menu['4'] = 'Usuń produkt'
        #  Na końcu jak już owarunkowane menu sie zbudowało to wyświetlamy
        for number, text in menu.items():
            print(f'{number}. {text}')
        self.get_choice()

    def get_choice(self):
        user_input = input('Wybierz numer: ')
        self.execute(user_input)

    def execute(self, user_input):
        if user_input == '1':
            self.show_products()
        if self.logged_in_user:
            if user_input == '2':
                self.add_product()
            if user_input == '3':
                self.logged_in_user = None
                self.show_menu()
            if user_input == '4':
                self.delete_product()
        else:  # <-- tutaj nie ma zalogowanego usera
            if user_input == '2':
                self.log_in()
        # Te dwie linijki poniżej wykonają się jeżeli żaden z 'ifów' wyżej nie spełni się
        self.show_menu()

    def add_product(self):
        for category in self.categories:
            print(category)
        category_name = input('Wybierz kategorię: ').lower()
        category = self.categories[category_name]
        name = input('Podaj nazwę produktu: ')
        size = input(f'Wybierz rozmiar produktu {category.get_sizes()}: ')
        new_product = ShopItem(name, size)
        new_product.category_name = category.category_name
        product_id = id(new_product)
        self.products[product_id] = new_product

    def log_in(self):
        user_input = input(f'Dostępni użytkownicy to {self.users}. Podaj login: ')
        for user in self.users:
            if user_input == user.login:
                self.logged_in_user = user
        self.show_menu()

    def show_products(self):
        for product_id, product in self.products.items():
            print(product_id, product.name, product.size, product.category_name)

    def delete_product(self):
        self.show_products()
        to_delete = input('Podaj id produktu do usunięcia: ')
        if int(to_delete) in self.products:
            self.products.pop(int(to_delete))
        self.show_menu()


karol = ShopWorker('karol', True)
pawel = ShopWorker('pawel')
users = [karol, pawel]
shoes = Category('buty')
clothes = Category('ciuchy')
supplements = Category('suplementy')
categories = {shoes.category_name: shoes, clothes.category_name: clothes, supplements.category_name: supplements}
ShopDataBase(users=users, categories=categories)

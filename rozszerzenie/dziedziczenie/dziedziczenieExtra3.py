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
    def __init__(self, category_name, name, size):
        super().__init__(category_name)
        self.name = name
        self.size = size

    def __str__(self):
        return f'{ self.name } - { self.size } ({self.category_name})'


class ShopWorker:
    def __init__(self, first_name, owner=False):
        self.first_name = first_name
        self.owner = owner

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return self.__str__()


class ShopDataBase:

    def __init__(self, users, categories, user=None, products={}):
        self.users = users
        self.user = user
        self.products = products
        self.categories = categories
        self.show()

    def show(self):
        menu = {
            '1': 'Lista produktów',
            '2': 'Dodaj produkt',
            '3': 'Zaloguj/Wyloguj',
            '4': 'Usuń produkt',
        }

        for number, text in menu.items():
            print(f'{number}. {text}')
        self.get_choice()

    def get_choice(self):
        user_input = input('Wybierz numer: ')
        self.execute(user_input)

    def execute(self, user_input):
        if user_input == '1':
            self.print_products()
            self.show()
        if self.user:
            if user_input == '2':
                self.add_product()
            if user_input == '3':
                self.log_out()
            if user_input == '4':
                self.delete_product()
        else:
            if user_input == '3':
                self.log_in()
            if user_input == '4':
                print('nie masz takiej opcji')
                self.show()
            self.show()

    def log_in(self):
        self.user = input('login: kim jesteś? ')
        self.show()

    def log_out(self):
        self.user = None
        print('wylogowałeś się!!!!!! ')
        self.show()
        return self.user

    def add_product(self):
        for category in self.categories:
            print(category)
        category_name = input('Wybierz kategorię: ').lower()
        category = self.categories[category_name]
        name = input('Podaj nazwę produktu: ')
        size = input(f'Wybierz rozmiar produktu {category.get_sizes()}: ')
        category_name = category.category_name
        new_product = ShopItem(category_name, name, size)
        product_id = id(new_product)
        self.products[product_id] = new_product
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
        if self.products:
            for product_id, product in self.products.items():
                print(product_id, product.name, product.size, product.category_name)
        else:
            print('lista produktów jest pusta')


owner = ShopWorker(owner=True, first_name='Karol')
worker = ShopWorker(owner=False, first_name='Paweł')

users = [owner, worker]
shoes = Category('buty')
clothes = Category('ciuchy')
supplements = Category('suplementy')
categories = {shoes.category_name: shoes, clothes.category_name: clothes, supplements.category_name: supplements}

ShopDataBase(users=users, categories=categories)

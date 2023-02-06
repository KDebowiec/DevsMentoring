# Zrób system, który obsługiwał będzie określone zamówienia. W programie istnieć będą 2 klasy:
# Manager oraz Order. W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia,
# a wartością jego ilość na stanie. W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena.
#
# Funkcjonalność programu to:
# - dodawanie nowego zamówienia do słownika (jeżeli dodawać będziemy obiekt, którego id
# znajduje się już w słowniku, to nie będziemy dodawali nowej pary do dicta, ale zwiększali ilość danego
# obiektu w słowniku (zwiększali odpowiednią wartość w słowniku)).
# - usuwanie o 1 zamówienia ze słownika o określonym id
import random


class Manager:
    def __init__(self):
        self.orders = {}
        self.menu()

    def menu(self):
        run = True
        while run:
            choice = int(
                input('co chcesz zrobić? 1 - dodać zamówienie, 2 - usunąć zamówienie, 3 - zobaczyć zamówienia,'
                      ' 4 - zakończyć program: '))
            if choice == 1:
                self.add_order()
            elif choice == 2:
                self.delete_order()
            elif choice == 3:
                self.show_orders()
            elif choice == 4:
                run = False

    def add_order(self):
        new_order = input('Dodaj zamówienie: ')
        amount = int(input('ile?: '))
        if new_order not in self.orders.keys():
            price = int(input('podaj cenę: '))
            order_id = random.randint(1, 1000)
            order = Order(order_id, new_order, price)
            self.orders.update({order_id: amount})
            print(f'{self.orders}')
        else:
            self.orders[new_order] += amount
            print(self.orders)

    def delete_order(self):
        which_one = input('jakie zamówienie chcesz usunąć?: ')
        how_much = int(input('ile?: '))
        if which_one in self.orders.keys():
            if self.orders[which_one] == 1:
                self.orders.pop(which_one)
                print(self.orders)
            else:
                self.orders[which_one] -= how_much
        else:
            print('nie ma takiego zamówienia')

    def show_orders(self):
        print(self.orders)


class Order:
    def __init__(self, order_id, name, price):
        self.name = name
        self.price = price
        self.order_id = order_id

    def __repr__(self):
        return f'{self.name} - {self.order_id}'


Manager()

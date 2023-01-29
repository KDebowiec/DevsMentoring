# Zrób system, który obsługiwał będzie określone zamówienia. W programie istnieć będą 2 klasy:
# Manager oraz Order. W Managerze ma się znajdować słownik zamówień, w którym kluczem będzie obiekt zamówienia,
# a wartością jego ilość na stanie. W klasie Order natomiast mają znajdować się takie pola jak: id, nazwa, cena.
#
# Funkcjonalność programu to:
# - dodawanie nowego zamówienia do słownika (jeżeli dodawać będziemy obiekt, którego id
# znajduje się już w słowniku, to nie będziemy dodawali nowej pary do dicta, ale zwiększali ilość danego
# obiektu w słowniku (zwiększali odpowiednią wartość w słowniku)).
# - usuwanie o 1 zamówienia ze słownika o określonym id
class Manager:
    def __init__(self):
        self.orders = {}
        self.add_order()

    def add_order(self):
        run = True
        while run:
            what_to_do = int(input('co chcesz zrobić? 1 - dodać zamówienie, 2 - usunąć zamówienie: '))
            if what_to_do == 1:
                choice = input('Dodaj zamówienie: ')
                if choice not in self.orders.keys():
                    price = int(input('podaj cenę: '))
                    order = Order(id, choice, price)
                    self.orders.update({order: 1})
                    print(self.orders)
                else:
                    self.orders[choice] += 1
                    print(self.orders)
            elif what_to_do == 2:
                which_one = input('jakie zamówienie chcesz usunąć?: ')
                if which_one in self.orders.keys():
                    self.orders.pop(which_one)
                else:
                    print('nie ma takiego zamówienia')


class Order:
    def __init__(self, id, name, price):
        self.id = id(Order)
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.choice}"


Manager()
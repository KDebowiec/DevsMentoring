# Stwórz klasę reprezentującą Prostokąt. Dodaj do niej metody obliczające pole i obwód
# z przechowywanych pól - szerokości i długości.
class Rectangle:
    def __init__(self, long_side, short_side):
        self.long_side = long_side
        self.short_side = short_side

    def count_area(self):
        area = self.long_side * self.short_side
        print(f'pole prostokąta to {area}')

    def count_circuit(self):
        circuit = 2 * self.short_side + 2 * self.long_side
        print(f'obwód prostokąta to {circuit}')


new_rectangle = Rectangle(10, 5)
new_rectangle.count_area()
new_rectangle.count_circuit()



# Stwórz klasę Shape i jej podklasę Square. Square ma posiadać konstruktor, który przyjmie length jako argument.
# Obie klasy mają posiadać metodę obliczającą pole figury. Domyślnie Shape ma zwracać wartość 0.
class Shape:
    def __init__(self, boki):
        self.boki = boki

    def pole(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__([length])

    def pole(self):
        length = self.boki[0]
        p = length * length
        return p



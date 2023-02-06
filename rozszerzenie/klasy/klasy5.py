# Stwórz program symulujący talię kart (klasa Deck) oraz pojedyncze karty (klasa Card).
# Karta ma być związana z takimi polami jak: wartość (np. 9) oraz figura (np. Diamond).
# W klasie Deck znajdować ma się lista reprezentująca stos kart w ramach jednej talii.
# W Deck znaleźć mają się takie metody jak: shuffle (która może wykorzystywać metodę o tej samej nazwie - shuffle - z
# biblioteki random) oraz deal (która będzie usuwała i zwracała ostatnią kartę z talii).

# Podpowiedź:
# Talia kart ma się składać z 52 różnych obiektów Card o wszystkich możliwych kombinacjach pól,
# np. (A - Diamond, A - Clubs itd). Aby utworzyć taką kombinację, utwórz dwie niezależne listy - w pierwszej
# przechowuj możliwe figury, a w drugiej wartości. Następnie przechodząc pętlami, łącz je ze sobą i twórz obiekty.
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.list_of_figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']
        self.list_of_colors = ['Trefl', 'Karo', 'Kier', 'Pik']

        self._populate_deck()

    def _populate_deck(self):
        for color in self.list_of_colors:
            for figure in self.list_of_figures:
                card = Card(color, figure)
                self.cards.append(card)

    def shuffle(self):
        run = True

        while run:
            choice = int(input("żeby przetasować talię, wciśnij 1: "))
            if choice == 1:
                new_deck = random.shuffle(self.cards)
                print(deck.cards)

    def deal(self):
        pass


class Card:
    def __init__(self, color, figure):
        self.color = color
        self.figure = figure

    def __str__(self):
        return f"{self.figure} {self.color}"

    def __repr__(self):
        return self.__str__()


deck = Deck()
new_deck = deck.shuffle()

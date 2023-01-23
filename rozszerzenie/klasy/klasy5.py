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
    list_of_figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']
    list_of_colors = ['Trefl', 'Karo', 'Kier', 'Pik']


class Card:
    def __init__(self, value, figure):
        self.value = value
        self.figure = figure

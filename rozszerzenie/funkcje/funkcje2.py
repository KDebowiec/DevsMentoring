# Czym się różni argument od parametru funkcji, default arguments od keyword arguments?

# Parametry deklarujemy na początku, po nazwie funkcji ale nie na nich będzie operowała funkcja, tylko na argumentach,
# czyli wartościach przypisanych parametrom. Parametr jest jak zmienna x, a argument to np. x = 2
#
# Keyword arguments używa się gdy w funkcji jest wiele argumentów i łatwo się pogubić, wtedy wywołując funkcje i
# przypisując jej argumenty, można je zadeklarować razem z parametrem do którego są przypisane np zamiast 'Jan'
# wpisujemy imie='Jan'
# Default arguments ustalamy na końcu listy parametrów z wykorzystaniem operatora przypisania. W sytuacji gdy nie przypiszemy
# im potem innej wartości, zostanie ona przypisana taka jak na początku
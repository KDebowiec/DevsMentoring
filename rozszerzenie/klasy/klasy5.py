# Stwórz program symulujący talię kart (klasa Deck) oraz pojedyncze karty (klasa Card).
# Karta ma być związana z takimi polami jak: wartość (np. 9) oraz figura (np. Diamond).
# W klasie Deck znajdować ma się lista reprezentująca stos kart w ramach jednej talii.
# W Deck znaleźć mają się takie metody jak: shuffle (która może wykorzystywać metodę o tej samej nazwie - shuffle - z
# biblioteki random) oraz deal (która będzie usuwała i zwracała ostatnią kartę z talii).

# Podpowiedź:
# Talia kart ma się składać z 52 różnych obiektów Card o wszystkich możliwych kombinacjach pól,
# np. (A - Diamond, A - Clubs itd). Aby utworzyć taką kombinację, utwórz dwie niezależne listy - w pierwszej
# przechowuj możliwe figury, a w drugiej wartości. Następnie przechodząc pętlami, łącz je ze sobą i twórz obiekty.


tab = []
file = open('pliki10_data.txt', 'r')
for line in file:
    tab.append(line.split())
file.close()

result = []

for i in range(200):
    for j in range(319):
        if abs(int(tab[i][j]) - int(tab[i][j + 1])) > 128:
            if [i, j] not in result:
                result.append([i, j])
            if [i, j + 1] not in result:
                result.append([i, j + 1])

for i in range(199):
    for j in range(320):
        if abs(int(tab[i][j]) - int(tab[i + 1][j])) > 128:
            if [i, j] not in result:
                result.append([i, j])
            if [i + 1, j] not in result:
                result.append([i + 1, j])

print(len(result))
print(result)
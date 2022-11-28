# Napisz program, który utworzy dwa zbiory:
# zbiór A: liczb naturalnych parzystych mniejszych od n (n podaje użytkownik)
# zbiór B: liczb naturalnych mniejszych od n, które przy dzieleniu przez 3 dają resztę
#  2 oraz zbiory będące wynikiem następujących operacji matematycznych:
#  C = A + B, D = A & B, E = A – B, F = B ^ A (różnica symetryczna)
#  Dla każdego z utworzonych zbiorów program poda informacje o jego nazwie,
# liczebności i zawartych w nim elementach. Na koniec program sprawdzi, czy zbiór B
#  zawiera się w zbiorze A.
n = int(input('podaj liczbę naturalną: '))
list_a = []
list_b = []

for i in range(1, n):
    list_a.append(i)

set_a = set(list_a)

for i in range(1, n):
    if i % 3 == 2:
        list_b.append(i)

set_b = set(list_b)

dict_of_sets = {'set a': set_a, 'set b': set_b, 'set c': set_a | set_b, 'set d': set_a & set_b,
                'set e': set_a - set_b, 'set f': set_a ^ set_b}

for i in dict_of_sets.keys():
    print(f'{i} ma {len(dict_of_sets[i])} elementów, oto one: ')
    print(dict_of_sets[i])

if set_a & set_b == set_b:
    print('zbiór B zawiera się w zbiorze A')
else:
    print("zbiór B nie zawiera sie w zbiorze A")
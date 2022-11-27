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
set_c = set_a | set_b
set_d = set_a & set_b
set_e = set_a - set_b
set_f = set_a ^ set_b

list_of_sets = [set_a, set_b, set_c, set_d, set_e, set_f]

for i in list_of_sets:
    print(f'{i} ma{len(i)} elementów, oto one: ')
    print(i)
#TODO w tej chwili zdanie wyjdzie "{1, 2, 3, 4, 5, 6, 7, 8, 9} ma9 elementów, oto one:" zamiast np set_a ma 9 elementów



if set_a & set_b == set_b:
    print('zbiór B zawiera się w zbiorze A')
else:
    print("zbiór B nie zawiera sie w zbiorze A")
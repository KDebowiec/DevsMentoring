# Napisz program, który utworzy dwa zbiory:
# zbiór A: liczb naturalnych parzystych mniejszych od n (n podaje użytkownik)
# zbiór B: liczb naturalnych mniejszych od n, które przy dzieleniu przez 3 dają resztę
#  2 oraz zbiory będące wynikiem następujących operacji matematycznych:
#  C = A + B, D = A & B, E = A – B, F = B ^ A (różnica symetryczna)
#  Dla każdego z utworzonych zbiorów program poda informacje o jego nazwie,
# liczebności i zawartych w nim elementach. Na koniec program sprawdzi, czy zbiór B
#  zawiera się w zbiorze A.


n = int(input('podaj liczbę naturalną: '))

set_a = {}
set_b = {}
set_c = {}
set_d = {}
set_e = {}
set_f = {}

list_a = []
list_b = []



for i in range (1,n):
    list_a.append(i)

set_a = set(list_a)

for i in range (1,n):
    if i % 3 == 2:
        list_b.append(i)

set_b = set(list_b)

set_c = set_a | set_b
set_d = set_a & set_b
set_e = set_a - set_b
set_f = set_a ^ set_b



print(f'zbiór A ma {len(set_a)} elementów, oto one: ')
for i in set_a:
    print(i, end = ' ')
print('\n')

print(f'zbiór B ma {len(set_b)} elementów, oto one: ')
for i in set_b:
    print(i, end = ' ')
print('\n')

print(f'zbiór C ma {len(set_c)} elementów, oto one: ')
for i in set_c:
    print(i, end = ' ')
print('\n')

print(f'zbiór D ma {len(set_d)} elementów, oto one: ')
for i in set_d:
    print(i, end = ' ')
print('\n')

print(f'zbiór E ma {len(set_e)} elementów, oto one: ')
for i in set_e:
    print(i, end = ' ')
print('\n')

print(f'zbiór F ma {len(set_f)} elementów, oto one: ')
for i in set_f:
    print(i, end = ' ')
print('\n')

if set_a & set_b == set_b:
    print('zbiór B zawiera się w zbiorze A')
else:
    print("zbiór B nie zawiera sie w zbiorze A")
# Utwórz dwie listy a i b. Sprawdź czy listy te mają chociaż jeden wspólny element.
a = ['a', 'b', 'c', 'd']
b = ['a', 'g', 'h', 'j']
c = []

for i in a:
    if i in b:
        c.append(i)

if c:
    print('Te listy mają chociaż jeden wspólny element')
else:
    print('nie mają wspólnego elementu')
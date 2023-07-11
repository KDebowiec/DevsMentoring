# Jaki efekt da poniższy zapis?
#
# examp = (i for i in range(10))
# print(examp)
#
# Jak należy zmienić kod, aby móc odczytywać kolejne liczby całkowite?

def example(limit):
    i = 0
    while i < limit:
        yield i
        i += 1


for i in example(100):
    print(i)

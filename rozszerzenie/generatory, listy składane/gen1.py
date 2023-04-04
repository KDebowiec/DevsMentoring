# Napisz funkcję generatora, która generować będzie kilka dowolnych wartości. Pobierz te wartości przy użyciu globalnej
# metody next() oraz metody generatora __next__().
# Rzuć wyjątkiem wewnątrz generatora (po jego kilkukrotnym wywołaniu) i zbadaj stack trace.
import random


# def generate_anything():
#     while True:
#
#         number = random.randint(1, 1000)
#         yield number
#
#
# generator = generate_anything()
#
# for i in range(5):
#     print(next(generator))

# ----------------------------------------


class Generate:

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            number = random.randint(1, 1000)
            return number


generate = Generate()

for i in range(5):
    print(next(generate))

# użyć metody send i throw w klasie generatora, żeby na podstawie wartości send rzucić wyjątkiem
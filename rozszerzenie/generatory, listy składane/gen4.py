# Stwórz generator zwracający kolejne wartości ciągu Fibonacciego. Do obliczania kolejnych wyrazów, wykorzystaj poniższy zapis:
#
# a = 1
# b = 2
# a, b = b, a + b

from collections.abc import Iterable, Iterator


class FibonacciIterable(Iterable):
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return FibonacciIterator(self.limit)


class FibonacciIterator(Iterator):
    def __init__(self, limit):
        self.iteration = 0
        self.a = 1
        self.b = 2
        self.limit = limit

    def __next__(self):
        result = self.a
        if self.limit < self.iteration:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.iteration += 1
        return result


fibonacci = FibonacciIterable(5)
for value in fibonacci:
    print(value)

#---------------to na co w powyższym jest iterator i iterable heee?--------------


class FibonacciIterator:
    def __init__(self, limit):
        self.iteration = 0
        self.a = 1
        self.b = 2
        self.limit = limit

    def __iter__(self):
        return FibonacciIterator(self.limit)

    def __next__(self):
        result = self.a
        if self.limit < self.iteration:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.iteration += 1
        return result


fibonacci = FibonacciIterator(5)
for value in fibonacci:
    print(value)

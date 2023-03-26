# Stwórz generator, który generował będzie kolejne liczby pierwsze.


#
class PrimeNumbers:
    def __init__(self, limit):
        self.number = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        while True:
            if self.number >= self.limit:
                raise StopIteration
            for divider in range(2, self.number):
                if self.number % divider == 0:
                    break
            else:
                return self.number
            self.number += 1


generator = PrimeNumbers(10)

for i in range(10):
    print(next(generator))

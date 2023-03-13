# Napisz dekorator @count, który wyświetlał będzie tworzył słownik, w którym będziemy przechowywali informację,
# ile razy zostały wywołane poszczególne funkcje udekorowane właśnie tym dekoratorem.
from functools import wraps


dictionary_of_functions = {}


def counting_calls(func):
    @wraps(func)
    def inner():
        func()
        if func.__name__ not in dictionary_of_functions:
            dictionary_of_functions.update({func.__name__: 1})
        else:
            for name in dictionary_of_functions:
                if name == func.__name__:
                    dictionary_of_functions[name] += 1

    return inner


@counting_calls
def write_number():
    print('10')


@counting_calls
def count():
    print(10 + 3)


write_number()
count()
count()
print(dictionary_of_functions)

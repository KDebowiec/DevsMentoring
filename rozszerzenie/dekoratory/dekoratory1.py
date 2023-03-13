# Zad. 1
# Napisz dekorator, który służyć będzie do logowania, z jakimi argumentami dana funkcja została wywołana.
# Skorzystaj z **kwargs, *args oraz zmiennej specjalnej __name__, aby logować również nazwę funkcji, którą wywołujemy.
#
# Kod:
def logged(func):
    def inner(*args):


    return inner

@logged
def func(*args):
   return 3 + len(args)

func(4, 4, 4)

# Output:
# you called func(4, 4, 4) it returned 6

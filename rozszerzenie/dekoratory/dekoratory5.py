# Utwórz dekorator @timethis mierzący czas wykonania dekorowanej funkcji. Wykorzystaj moduł time i metodę time.time().
import time


def function_duration(func):
    def inner():

        start_time = time.time()
        func()
        end_time = time.time()

        duration = end_time - start_time
        print(f'funkcja wykonała się w {duration} sekund')
    return inner


@function_duration
def call():
    x = []
    for i in range(10000000):
        x.append(i)
    print(x)


call()
# Stwórz dekorator, który będzie służył do przyozdabiania wyświetlanego tekstu gwiazdkami.
# Dowolny tekst ten ma być wyświetlany z poziomu dekorowanej funkcji.

# Efekt:
# ************
# Hello World!
# ************
def decorating(func):
    def inner(x):
        print(10 * '*')
        func()
        print(10 * '*')

    return inner


@decorating
def func():
    print(x)

x = input('podaj zdanie: ')
func(x)
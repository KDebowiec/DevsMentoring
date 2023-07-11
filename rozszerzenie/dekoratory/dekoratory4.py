# W szkoleniu nie zostało o tym wspomniane, ale możemy również określać przesyłane argumenty dekoratorów!
# Jedyna konieczność jaka będzie do zrealizowania, to dodanie kolejnej funkcji wrappującej, czyli np:
#
# def arg_check(arg):
#     def check(old_func):
#         def new_func():
#
#         # do sth with arg and call old_func as examp
#
#         return new_func
#
#     return check
#
# @arg_check(arg)
# def examp(num):


# Twoje zadanie to stworzyć dekorator, który sprawdzać będzie, czy określony w dekoratorze typ jest zgodny
# z typem zmiennej przesłanej do funkcji.
#
# Podpowiedź:
# Przesyłaj jako argument do dekoratora obiekt typu: int, float itd
# Sprawdzaj, czy typy są zgodne przy użyciu isinstance(zmienna, typ_oczekiwany)
# Jeżeli typ będzie niezgodny, rzucaj wyjątkiem

def check(func):
    def inner(arg):
        func(arg)
    return inner

@check
def bla():
    pass

def arg_check(arg):
    def check(old_func):
        def new_func(func_arg):
            print(isinstance(func_arg, arg))
            old_func(func_arg)
        return new_func
    return check




@arg_check(int)
def examp(num):
    print(num)


examp(12)

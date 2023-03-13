from functools import wraps


def decorating(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        for number in args:
            if type(number) == int:
                print(f'{number} is number')
            else:
                print(f'{number} is not a number')
        for key in kwargs:
            if type(kwargs[key]) == int:
                print(f'{kwargs[key]} is number')
            else:
                print(f'{kwargs[key]} is not a number')

    return inner

@decorating
def write_number(number):
    print(f'Your number is {number}')

write_number(10)
write_number('dziesięć')
print(write_number.__name__)


# def decorating(func):
#     def inner(number):
#         func(number)
#         if type(number) == int:
#             print(f'{number} is number')
#         else:
#             print(f'{number} is not a number')
#
#     return inner
#
# @decorating
# def write_number(number):
#     print(f'Your number is {number}')
#
# write_number(10)
# write_number('dziesięć')
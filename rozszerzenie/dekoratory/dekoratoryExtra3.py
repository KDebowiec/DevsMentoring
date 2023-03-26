def printing_hello(*args):

    def wrapper(function):

        def hello(function_arg):
            print('hello')
            function(function_arg)

        return hello
    return wrapper


@printing_hello(str)
def printing(name):
    print(f'{name}')


printing('Magda')
import datetime


def simple_current_time_wrapper(arg):

    def add_datetime(old_func):
        def new_func(func_arg):

            print(datetime.datetime.now())
            old_func(func_arg)

        return new_func
    return add_datetime


@simple_current_time_wrapper(str)
def print_greetings(name):
    print(f'Hello {name}!')


print_greetings('Karol')
def best_score(args):

    def add_best(old_func):

        def adding(*args):
            a = 0

            for arg in args:
                if arg > a:
                    a = arg

            print(f'najwyzsza ocena to {a}')
            old_func(args)

        return adding

    return add_best


@best_score(tuple)
def counting_grade_average(args):

    av = sum(args) / len(args)
    print(f'średnia ocen to : {av}')


counting_grade_average(1, 2, 4, 6)

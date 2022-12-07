# Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. W funkcji dokonaj ich połączenia w jedną listę
# w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]
def one_list(**kwargs):
    new_list = []

    for element in kwargs['kwarg_1']:
        new_list.append(element)
        new_list.append(kwargs['kwarg_2'][(kwargs['kwarg_1'].index(element))])
    print(new_list)


def main():
    one_list(kwarg_1=[1, 3, 5, 7], kwarg_2=[2, 4, 6, 8])


if __name__ == '__main__':
    main()




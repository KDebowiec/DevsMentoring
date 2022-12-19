# Prześlij przy użyciu **kwargs listę liczb parzystych i nieparzystych. W funkcji dokonaj ich połączenia w jedną listę
# w następujący sposób: [nieparzysta, parzysta nieparzysta, parzysta ...]
# def one_list(**kwargs):
#     new_list = []
#
#     for element in kwargs['kwarg_1']:
#         new_list.append(element)
#         second = kwargs['kwarg_1'].index(element)
#         new_list.append(kwargs['kwarg_2'][(second)])
#     print(new_list)

def one_list(**kwargs):
    list_1 = kwargs.get("kwarg_1")
    list_2 = kwargs.get("kwarg_2")
    new_list = []

    if len(list_1) > len(list_2):
        iterations = len(list_2)
        for i in range(iterations):
            new_list.append(list_1[i])
            new_list.append(list_2[i])
        for i in range(len(list_2), len(list_1)):
            new_list.append(list_1[i])

    else:
        iterations = len(list_1)
        for i in range(iterations):
            new_list.append(list_1[i])
            new_list.append(list_2[i])
        for i in range(len(list_1), len(list_2)):
            new_list.append(list_2[i])

    return new_list


def main():
    print(one_list(kwarg_1=[1, 3, 5, 7, 9], kwarg_2=[2, 4, 6, 8]))


if __name__ == '__main__':
    main()


#TODO użyj pop
# TODO poprawione tak żeby działało dla list o różnych długościach
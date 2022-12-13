# Napisz funkcję, która jako argument przyjmuje 10-cio elementową listę liczb całkowitych. Ma ona zwrócić przefilitrowaną
# listę elementów składającą się tylko z liczb dwucyfrowych wyselekecjonowanych z odebranej listy.
def selection(list_):
    new_list = []
    for elements in list_:
        if 100 > elements > 9:
            new_list.append(elements)

    print(new_list)


def main():
    list_ = [1, 2, 4, 10, 23, 43, 2, 5, 12, 144]
    selection(list_)


if __name__ == '__main__':
    main()

#TODO poprawione żeby nie używać args
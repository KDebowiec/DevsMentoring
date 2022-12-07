# Napisz funkcję, która jako argument przyjmuje 10-cio elementową listę liczb całkowitych. Ma ona zwrócić przefilitrowaną
# listę elementów składającą się tylko z liczb dwucyfrowych wyselekecjonowanych z odebranej listy.
def selection(*args):
    new_list = []
    for elements in args:
        for number in elements:
            if number < 10:
                new_list.append(number)

    print(new_list)


def main():
    list_ = [1, 2, 4, 10, 23, 43, 2, 5, 12, 144]
    selection(list_)


if __name__ == '__main__':
    main()
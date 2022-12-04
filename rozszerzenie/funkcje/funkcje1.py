# Zdefinuj funkcję, która znajdzie i zwróci indeks największego elementu z przekazanej jako parametr listy
#
# nums = [4, 6, 8, 24, 12, 2]
#
# Dodatkowo:
# Zapoznaj się funkcją enumerate z dokumentacji https://book.pythontips.com/en/latest/enumerate.html.
# Spróbuj ją zastosować w rozwiązaniu powyższego zadania.

def searching_for_biggest(nums):
    for counter, value in enumerate(nums):
        if value is max(nums):
            print(f'indeks największego elementu listy to {counter}')


def main():
    nums = [4, 6, 8, 24, 12, 2]
    searching_for_biggest(nums)


if __name__ == '__main__':
    main()
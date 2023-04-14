def example1():
    for i in range(3):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        try:
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError:
            print('Cant Divide')


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    try:
        for i in range(len(L)):
            sumOfPairs.append(L[i] + L[i + 1])
    except IndexError:
        print('List index out of range')
    except TypeError:
        print('one of elements is wrong type')

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        print('there is no such h file in this directory')

    try:
        for line in file:
            print(line.upper())
        file.close()
    except UnboundLocalError:
        print('file is not associated with value')

def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


if __name__ == '__main__':
    main()
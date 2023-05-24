# Stwórz program, który będzie sortował dziesięć 100-elementowych tablic z wykorzystaniem bubble sorting
# w podejściu wielowątkowym (multithreading) oraz wieloprocesowym (multiprocessing). Porównaj czasy.
#
# Rozważ również problem:
# Ile wątków należy stworzyć, aby program był wykonany jak najszybciej i optymalnie?
# Aby odpowiedzieć na to pytanie, zapoznaj się z “Amdahl’s Law”.
import time
from threading import Thread
from multiprocessing import Pool


array = [
    [1, 5, 4, 6],
    [12, 3, 55, 2],
    [8, 9, 22, 33],
    [100, 0, 7, 99]
]

list_to_sort = [5, 2, 3, 22, 7]


def sorting(matriz):
    i = 0
    while i < len(list_to_sort)-1:
        j = 0
        while j < len(list_to_sort) - 1 - i:
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
            j += 1
        i += 1
    print(list_to_sort)


def sorting2(matriz):
    for element in array:
        i = 0
        while i < len(element)-1:
            j = 0
            while j < len(element) - 1 - i:
                if element[j] > element[j+1]:
                    element[j], element[j + 1] = element[j + 1], element[j]
                j += 1
            i += 1
    print(array)


sorting2(array)

if __name__ == '__main__':
    t1 = Thread(target=sorting, args=[list_to_sort])
    t2 = Thread(target=sorting, args=[list_to_sort])

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print('Time taken in seconds for multithreading-', end - start)

if __name__ == '__main__':
    pool = Pool(processes=2)
    start2 = time.time()
    p1 = pool.apply_async(sorting, [list_to_sort])
    p2 = pool.apply_async(sorting, [list_to_sort])
    pool.close()
    pool.join()
    end2 = time.time()
    print('Time taken in seconds for  simultaneous-', end2 - start2)


# W pewnej grze liczbowej wylosowano następujące liczby:
# wynik = [12,1,45,76,50,23]. Okazało się jednak, że wylosowane wartości powinny zawierać się
# w przedziale od 1 do 49. Napisz program zastępujący dowolne liczby – nie tylko te konkretne z
# zadania - występujące w liście, które nie spełniają tego kryterium, na wylosowane liczby, które
# będą je spełniać. Program powinien także zakomunikować, że znalazł błędną wartość i dokonał dla niej zmiany.

import random

numbers_list = [12, 1, 45, 76, 50, 23]


for i in numbers_list:
    if i < 1 or i > 48:
        print(f'liczba {i} zostanie zastąpiona')
        valid_number = random.randint(1, 49)

        index = numbers_list.index(i)
        numbers_list[index] = valid_number

print(numbers_list)


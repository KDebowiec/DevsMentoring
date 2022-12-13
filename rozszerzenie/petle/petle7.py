# Napisz program wyznaczający n (podawane przez użytkownika) pierwszych liczb ciągu Fibonacciego. Przykład:
# dla n = 5
# 0, 1, 1, 2, 3, 5
# Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.
number = int(input('podaj liczbę: '))

list_fibonacci = [0, 1]

for i in range(number-2):
    num_1 = list_fibonacci[i]
    num_2 = list_fibonacci[i+1]

    list_fibonacci.append(num_1+num_2)

print(list_fibonacci)
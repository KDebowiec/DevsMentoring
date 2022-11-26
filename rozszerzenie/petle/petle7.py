# Napisz program wyznaczający n (podawane przez użytkownika) pierwszych liczb ciągu Fibonacciego. Przykład:
# dla n = 5
# 0, 1, 1, 2, 3, 5
# Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.
number = int(input('podaj liczbę: '))
list_of_all = []
list_fibonacci = []
for i in range(number+1):
    list_of_all.append(i)

print(list_of_all)

if list_of_all[i] in list_of_all == list_of_all[i-2] + list_of_all[i-1]:
    list_fibonacci.append((list_of_all[i]))

print(list_fibonacci)

#TODO dokończyć
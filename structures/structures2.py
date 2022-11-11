last_number = int(input('podaj liczbę: '))
list1 = []
value = 0


for i in range(last_number):
    i = i+1
    list1.append(i)

print(sum(list1))
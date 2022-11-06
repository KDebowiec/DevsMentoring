list=[]
number=0

for i in range (10):
    number=int(input('podaj liczbę: '))
    list.append(number)


for number in list:
    if number %2 == 0:
        print(number)
    else:
        continue
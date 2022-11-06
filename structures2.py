last_number = int(input('podaj liczbę: '))
list=[]
value=0


for i in range(1,last_number):
    i=i+1
    list.append(i)

list.append(1)
print(sum(list))
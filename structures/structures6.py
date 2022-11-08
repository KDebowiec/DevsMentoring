a = [3, 1, 5, 7, 9, 2, 6]

print(a[3])    #element o indeksie 3 z listy a
print(a[1:4])  #elementy z listy a o indeksach z zakresu 1-4
print(a[3:])   #elementy z listy a o indeksach od 3 w górę
print(a[-3:])  #elementy z listy a, 3 elementy od końca
print(a[:3])   #elementy z lsty a, o indeksach od 0 do 3 wyłącznie
print(a[3:-1]) #elementy z listy a, o indeksacch od 3 do 1 od końca wyłącznie
print(a[::2])  #co drugi element z listy a
print(a[5:2:-1])#elementy z listy a, o indeksach od 5 do 2 wyłącznie, krok o -1
print(sum(a))  #suma elementów listy a
print(8 in a)  #sprawdzamy czy 8 należy do listy a - nie należy
print(4 not in a) # sprawdzamy czy 4 NIE należy do listy a, nie należy więc TRUE
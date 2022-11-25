# Napisz program, który będzie pracował z trzema listami:
# lista1 = ["abc", "def", "ghi", "jkl"]
# lista2 = [1, 2, 3, 4, 5]
# lista3 = ["xyz", 1, '2']
#
# Niech program:
# • wydrukuje te listy
# • wydrukuje pierwszy oraz czwarty element z lista1
# • przypisze drugiemu elementowi lista2 wartości drugiego elementu z lista3
# • przypisze trzeciemu elementowi lista3 wartość tekstową wpisaną z klawiatury
# • doda nowy element ‘słowo’ do lista1 za pomocą metody .append()
# • skasuje element o indeksie 2 z lista1
# • wyznaczy liczbę elementów lista3
# • powiększy lista1 o elementy lista3
# Po każdej przeprowadzonej zmianie wydrukuje zmienioną listę.


lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2']
lista4 = [lista1, lista2, lista3]

for i in lista4:
    print(i)
print(lista1[0], lista1[3])

lista2[1] = lista3[1]
print(lista2)

new_element = (input('wpisz tekst który zastąpi trzeci element listy nr 3: '))
lista3[2] = new_element
print(lista3)

lista1.append('słowo')
print(lista1)

lista1.pop(2)
print(lista1)

print(f'długosc listy 3 to {len(lista3)}')

lista1 = lista1 + lista3
print(lista1)
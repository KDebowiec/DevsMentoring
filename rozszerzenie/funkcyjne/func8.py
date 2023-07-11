# Wyobraź sobie, iż masz do dyspozycji następującą listę 4 zamówionych produktów o następujących właściwościach: id, nazwa, ilość, cena.
#
# orders = [
# ["34587", "Learning Python, Mark Lutz", 4, 40.95],
# ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],
# ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
# ]
#
# Twoim zadaniem jest stworzenie programu budującego fakturę dla powyższej listy. Lista ta ma zawierać krotki,
# które przechowywać będą kolejno id danego produktu i cenę, jaką należy za niego zapłacić. Jednak istnieje pewne
# dodatkowe utrudnienie - wartość zamówień poniżej 100 zł, musi być zwiększana o 10. Czyli wynikiem dla powyższej listy będzie:
#
# invoice = [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001), ('88112', 84.97)]

orders = [
["34587", "Learning Python, Mark Lutz", 4, 40.95],
["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],
["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]

invoice = list(map(lambda x: (x[0], x[2]*x[3] if x[2]*x[3] >= 100 else x[2]*x[3] + 10), orders))
print(invoice)

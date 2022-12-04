# Zad 5.
# Program ma tworzyć rachunek za prestiżową kolację w restauracji dla poszczególnych osób.
#
# Dla przykładowej listy:
#
# bill_items = [
#     ['Tom', 'Calamari', 6.00],
#     ['Tom', 'American Hot', 11.50],
#     ['Tom', 'Chocolate Fudge Cake', 4.45],
#     ['Clare', 'Bruschetta Originale', 5.35],
#     ['Clare', 'Fiorentina', 10.65],
#     ['Clare', 'Tiramisu', 4.90],
#     ['Rich', 'Bruschetta Originale', 5.35],
#     ['Rich', 'La Reine', 10.65],
#     ['Rich', 'Honeycomb Cream Slice', 4.90],
#     ['Rosie', 'Garlic Bread', 4.35],
#     ['Rosie', 'Veneziana', 9.40],
#     ['Rosie', 'Tiramisu', 4.90],
# ]
#
# Wynikiem ma być słownik w postaci:
# {
# ‘Tom’ : {‘potrawy’ : [‘Calamari’, ‘American Hot’, ‘Chocolate Fudge Cake’], ‘cena’ : 21.95},
# ‘Clare’ : {‘potrawy : [‘Bruschetta Originale‘, ‘Fiorentina’, ‘Tiramisu’], ‘cena’ : 20.90},
# …
# }
bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]
Tom_dishes = []
Tom_price = 0
Claire_dishes = []
Claire_price = 0
Rich_dishes = []
Rich_price = 0
Rosie_dishes = []
Rosie_price = 0
final_bill = {}

for i in bill_items:
    if i[0] == 'Tom':
        Tom_dishes.append(i[1])
        Tom_price = Tom_price + i[2]
        Tom = {}
        Tom.update({'potrawy': Tom_dishes})
        Tom.update({'cena': Tom_price})
        final_bill.update({'Tom': Tom})
    if i[0] == 'Claire':
        Claire_dishes.append(i[1])
        Claire_price = Claire_price + i[2]
        Claire = {}
        Claire.update({'potrawy': Claire_dishes})
        Claire.update({'cena': Claire_price})
        final_bill.update({'Claire': Claire})
    if i[0] == 'Rich':
        Rich_dishes.append(i[1])
        Rich_price = Rich_price + i[2]
        Rich = {}
        Rich.update({'potrawy': Rich_dishes})
        Rich.update({'cena': Rich_price})
        final_bill.update({'Rich': Rich})
    if i[0] == 'Rosie':
        Rosie_dishes.append(i[1])
        Rosie_price = Rosie_price + i[2]
        Rosie = {}
        Rosie.update({'potrawy': Rosie_dishes})
        Rosie.update({'cena': Rosie_price})
        final_bill.update({'Rosie': Rosie})

print(final_bill)


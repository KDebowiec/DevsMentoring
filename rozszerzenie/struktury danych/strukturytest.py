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
final_bill = {}
names_list = ['Tom', 'Clare', 'Rich', 'Rosie']

for i in bill_items:
    for y in names_list:
        if i[0] == y:

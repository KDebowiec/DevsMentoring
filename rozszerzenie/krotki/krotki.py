# Utwórz listę składającą się z następujących elementów: 'zielony', 'czerwony', 'niebieski',
# 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony', 'cytrynowy',
# 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'.
# Przekształć tę listę w zbiór i zachowaj pod nową nazwą, a następnie:
# policz, ile elementów zawiera oryginalna lista kolorów
# policz, ile różnych kolorów zostało użytych
# wyświetl każdy z elementów zbioru w oddzielnej linii
# dodaj do zbioru nazwę jakiegoś innego koloru (sprawdź efekt przez wyświetlenie zawartości)
# usuń ze zbioru jakiś kolor (ponownie sprawdź efekt)

colors = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebiesko' , 'czarny',
          'czarny', 'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

colors_new = set(colors)

print(f'lista colors ma  {len(colors)} elementów')

colors_list = list(colors_new)
print(f'zostało użytych {len(colors_list)} kolorów')

for i in colors_list:
    print(i)

colors_new.update({'seledynowy'})
print(colors_new)

colors_new.discard('czarny')
print(colors_new)
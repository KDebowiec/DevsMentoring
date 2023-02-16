# class Manager:
#     def __init__(self):
#         self.order = {}
#         self.add_order()
#
#     def add_order(self):
#         run = True
#         while run:
#             what_to_do = int(input('co chcesz zrobić? 1 - dodać zamówienie, 2 - usunąć zamówienie: '))
#             if what_to_do == 1:
#                 choice = input('Dodaj zamówienie: ')
#                 if choice not in self.order.keys():
#                     price = int(input('podaj cenę: '))
#                     order = Order(id, choice, price)
#                     self.order.update({order: 1})
#                     print(self.order)
#                 else:
#                     self.order[choice] += 1
#                     print(self.order)
#             elif what_to_do == 2:
#                 which_one = input('jakie zamówienie chcesz usunąć?: ')
#                 if which_one in self.order.keys():
#                     self.order.pop(which_one)
#                 else:
#                     print('nie ma takiego zamówienia')
#
#
# class Order:
#     def __init__(self, id, name, price):
#         self.id = id(Order)
#         self.name = name
#         self.price = price
# test_dict = {'name': {'capacity': 'capacity', 'volume': 0}, 'namgffe': {'capadhgfcity': 'capadhcity', 'volume': 'vofglume'}, 'nafgme': {'capadfhcity': 'capadfhcity', 'volume': 'vofdhglume'}}
# second_dict = []
# for name in test_dict:
#     for volume in test_dict[name]['volume']:
#         if volume == 0:
#             second_dict.append(test_dict[name]['volume'])
# print(second_dict)

# for name, capacity in test_dict.items():
#     print(name, capacity['volume'])
#
# for name in test_dict:
#     second_dict.update({name: test_dict[name]['volume']})
# print(second_dict)
# prefiks = {'karol': 12, 'przemek': 123, 'konrerthgtrergfad': 8}
# print(max(prefiks))

# tank_dict = {'zbiornik1': {'capacity': 1000, 'volume': 800},
#              'zbiornik2': {'capacity': 900, 'volume': 300},
#              'zbiornik3': {'capacity': 1100, 'volume': 1100}}

FAILED_OPERATIONS = [{'zbiornik1': {'time': 12, 'operation_name': 'pour', 'ilość wody': 400, 'succes': True}},
                     {'zbiornik1': {'time': 12, 'operation_name': 'pour', 'ilość wody': 400, 'succes': False}}]


for dict_ in FAILED_OPERATIONS:
    for i in dict_:
        if dict_[i]['succes']:
            print(dict_)

# for dict_ in FAILED_OPERATIONS:
#     if 'zbiornik1' in dict_:
#         if dict_["zbiornik1"]["operation_name"] == 'pour':
#             print('typ operacji: dolewanie wody do zbiornika')
#         elif dict_["zbiornik1"]["operation_name"] == 'pour_out_water':
#             print('odlewanie wody ze zbiornika')
#         elif dict_["zbiornik1"]["operation_name"] == 'add_tank':
#             print('dodawanie zbiornika')
#         print (f'data i czas: {dict_["zbiornik1"]["time"]}, '
#               f'ilość wody: {dict_["zbiornik1"]["ilość wody"]}, ')
#         if dict_["zbiornik1"]["succes"]:
#             print('operacja zakończona sukcesem')
#         else:
#             print('operacja nieudana')

# Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik, na którym była ona wykonana
# oraz ilość wody, jaka była brana pod uwagę oraz to, czy operacja się powiodła czy nie.
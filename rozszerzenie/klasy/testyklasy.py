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
listX = [2, 3, 6, 8]
print(listX.index(3))
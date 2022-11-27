my_favourites = {'zielony', 'niebieski', 'czarny'}
user_favourites =input("podaj ulubione kolory, w jednej linii oddzielone spacjami: ")

user_favourites_list = user_favourites.split()
user_favourites_set = set(user_favourites_list)
mutual_elements = []
only_my = []
users_only = []


if my_favourites != user_favourites_set:
    if my_favourites & user_favourites_set != 0:
        print(f'oboje wybralismy {my_favourites & user_favourites_set}')
    else:
        print('podobają nam się inne kolory')
    if my_favourites - user_favourites_set != 0:
        print(f'tylko ja wybrałem {my_favourites - user_favourites_set}')
    if user_favourites_set - my_favourites != 0:
        print(f'tylko ty wybrałeś {user_favourites_set - my_favourites}')

else:
    print('wybraliśmy takie same kolory')

# for i in my_favourites:
#     if i in user_favourites_set:
#         mutual_elements.append(i)
#     else:
#         only_my.append(i)
#
# for i in user_favourites_set:
#     if i not in my_favourites:
#         users_only.append(i)
#
# print(mutual_elements)
# print(only_my)
# print(users_only)
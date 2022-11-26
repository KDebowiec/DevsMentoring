my_favourites = {'zielony', 'niebieski', 'czarny'}

user_favourites =input("podaj ulubione kolory, w jednej linii oddzielone spacjami: ")
user_favourites_list = user_favourites.split()
user_favourites_set = set(user_favourites_list)

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

    
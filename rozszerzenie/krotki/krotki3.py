# Napisz program, który poprosi użytkownika o podanie zestawu ulubionych przez niego kolorów (dowolna liczba).
# Kolory powinny być wpisane w jednej linii jako tekst i rozdzielone spacją.
# W programie powinien znajdować się zbiór Twoich ulubionych kolorów. Należy porównać oba zbiory:
# Twój i użytkownika oraz sprawdzić, czy są jednakowe.

# Jeśli tak, należy wydrukować odpowiedni komentarz, jeśli nie należy podać te kolory, które:
# wybrały obie osoby
# wybrał tylko użytkownik
# preferuje jedynie autor programu

my_favourites = {'zielony', 'niebieski', 'czarny'}
user_favourites = input("podaj ulubione kolory, w jednej linii oddzielone spacjami: ")

user_favourites_list = user_favourites.split()
user_favourites_set = set(user_favourites_list)


if my_favourites != user_favourites_set:
    if my_favourites & user_favourites_set:
        print(f'oboje wybralismy {my_favourites & user_favourites_set}')
    else:
        print('podobają nam się inne kolory')

    if my_favourites - user_favourites_set:
        print(f'tylko ja wybrałem {my_favourites - user_favourites_set}')

    if user_favourites_set - my_favourites:
        print(f'tylko ty wybrałeś {user_favourites_set - my_favourites}')

else:
    print('wybraliśmy takie same kolory')
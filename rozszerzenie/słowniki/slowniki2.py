# Zmodyfikuj kod z zadania 1 tak, aby możliwe było dodawanie i usuwanie przez użytkownika informacji
# o nowych albumach do słownika. Program ma zawierać proste menu.
choice = 0
Album = None
Singer = None
new_album = None
new_singer = None
delete_key = None


def menu():
    print(' 1 - sprawdź wykonawce \n 2- dodaj album do bazy \n 3 - usuń album  \n'
          ' 4 - zakończ')
    choice = int(input('co chcesz zrobić? '))


dictionary_1 = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2',
                'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

for key in dictionary_1:
    print(key, end=', ')
print('\n')

print('witaj w programie \n 1 - sprawdź wykonawce \n 2- dodaj album do bazy \n 3 - usuń album  \n'
      ' 4 - zakończ')
choice = int(input('co chcesz zrobić? '))

while choice in range(1, 5):
    if choice == 1:
        Album = input('podaj album którego wykonawce chcesz poznać: ')
        if Album in dictionary_1:
            Singer = dictionary_1.get(Album)
            print(f'wykonawcą {Album} jest {Singer}')
            menu()
        else:
            print('Nie ma takiego albumu')
            menu()
    elif choice == 2:
        new_singer = input('podaj wokalistę: ')
        new_album = input('podaj album: ')
        dictionary_1.update({new_album: new_singer})
        print('dodałeś nowy album i jego wykonawce do bazy!')
        menu()
    elif choice == 3:
        delete_key = input('podaj album który chcesz usunąć: ')
        del dictionary_1[delete_key]
        print('usunąłeś ten Album!')
        menu()
    elif choice == 4:
        print('koniec programu')
else:
    print('podaj właścwą cyfrę')
    menu()

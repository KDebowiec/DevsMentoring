# Wprowadź poniższy słownik do programu. Program ma działać, tak jak poniżej:
# • wyświetla wszystkie klucze na konsoli (tzn. nazwy wszystkich albumów),
# • pobiera od użytkownika łańcuch i sprawdza czy odpowiada on kluczowi ze słownika.
#
# Jeśli tak, to wyświetlany jest odpowiedni komunikat, np.: "Wykonawcą albumu "Achtung baby" jest “U2".
# W przeciwnym razie wyświetlany jest komunikat: "Brak danych".
#
# {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' :
#     'Dead Can Dance', 'Invisible Touch' : 'Genesis'}
dictionary_1 = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2',
                'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}

for key in dictionary_1:
    print(key, end = ', ')
print('\n')

while True:
    Album = input('podaj album którego wykonawce chcesz poznać: ')
    while Album in dictionary_1:
        Singer = dictionary_1.get(Album)
        print(f'wykonawcą {Album} jest {Singer}')
        Album = input('podaj album którego wykonawce chcesz poznać: ')
    else:
        print('Nie ma takiego albumu')


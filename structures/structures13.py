# Zad 13.
# Utwórz słownik, który przechowuje definicje wyrazów i ich wytłumaczenia. Zarządzanie słownikiem ma się odbywać
# za pomocą interaktywnego MENU (MENU ma być obsługiwane za pomocą print() oraz input() oraz ma wyglądać tak jak poniżej):
# 1. Dodaj słowo wraz z definicją
# 2. Znajdź definicję słowa
# 3. Usuń słowo wraz z definicją z słownika
# 4. Zakończ program



dictionary = {'dog': 'pies', 'cat': 'kot', 'cow': 'krowa'}
necessary_word = 0
unnecessary_word = 0
eng_word = None
pol_word = None

print('1 - dodaj słowo z definicją')
print('2 - znajdź definicję')
print('3 - usuń słowo i jego definicje ze słownika')
print('4 - zakończ działanie programu')

while True:
    add_word = int(input('co chcesz zrobić? '))
    if add_word == 1:
        eng_word = input('podaj angielskie słowo ')
        pol_word = input('podaj definicje po polsku ')
        dictionary.update({eng_word: pol_word})
    elif add_word == 2:
        necessary_word = input('powiedz jakie słowo chcesz przetłumaczyć: ')
        if necessary_word in dictionary:
            print(dictionary[necessary_word])
        else:
            print('tego słowa nie ma w słowniku')
    elif add_word == 3:
        unnecessary_word = input('powiedz jakie słowo chcesz usunąć ze słownika ')
        del dictionary[unnecessary_word]
        print('slowo zostało usunięte')
    elif add_word == 4:
        print('kończenie pracy programu')
        break


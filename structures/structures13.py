dictionary = {'dog': 'pies', 'cat': 'kot', 'cow': 'krowa'}
necessary_word = 0
unnecessary_word = 0

print('1 - dodaj słowo z definicją')
print('2 - znajdź definicję')
print('3 - usuń słowo i jego definicje ze słownika')
print('4 - zakończ działanie programu')

add_word = int(input('co chcesz zrobić? '))
eng_word = None
pol_word = None

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
# elif add_word == 3:
#     unnecessary_word = input('powiedz jakie słowo chcesz usunąć ze słownika')
#     dictionary.discard(unnecessary_word)

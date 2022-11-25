# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), a
# następnie korzystając z metod operujących na listach, program powinien:
# • podawać liczbę wyrazów w zdaniu
# • podawać wyrazy, które rozpoczynają się wielką literą, jeśli takie są, jeśli nie, również to zgłosić
# • sprawdzać i podawać, czy lista zawiera: „i”, „w”, „na”, „pod”, „dla”. Jeśli tak, to które są to wyrazy
# i jakie są ich indeksy na liście. Jeśli żaden z poszukiwanych wyrazów w zdaniu nie występuje program
# również powinien o tym informować
# • posortować wyrazy ze zdania alfabetycznie i wydrukować je w zmienionej kolejności.
import re

sentence = None
new_text = None
sentence_list = []
big_letters = []
list_of_words = []
special_words = ['i', 'na', 'pod', 'dla', 'w']

sentence = input('wpisz zdanie: ')
x = sentence.replace('!', '')
x = x.replace('?', '')
x = x.replace('.', '')
x = x.replace(',', '')
x = x.replace(';', '')
x = x.replace(':', '')
x = x.replace('/', '')
x = x.replace('(', '')
x = x.replace(')', '')
new_text = x.replace('-', '')
sentence_list = new_text.split()
print(f'liczba wyrazów w zdaniu to {len(sentence_list)}')

for i in sentence_list:
    if not str.islower(i):
        big_letters.append(i)
    else:
        continue
if big_letters:
    print('te wyrazy zaczynają się dużą literą:')
    for i in big_letters:
        print(i, end = ' ')
else:
    print("zaden wyraz nie zaczyna sie dużą literą")

for i in sentence_list:
    if i in special_words:
        print(f'{i} znaleziono w zdaniu')
        print(f'indeks tego słowa to {sentence_list.index(i)}')
        list_of_words.append(i)


if not list_of_words:
    print('żadne z tych słów nie znalazło się w zdaniu')

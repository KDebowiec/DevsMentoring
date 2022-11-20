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

sentence = input('wpisz zdanie: ')
new_text = re.sub(r"[^a-zA-Z0-9 ]", "", sentence)
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

print('\n')
for i in sentence_list:
    if i == 'i' or 'w' or 'na' or 'pod' or 'dla':
        print(f'{i} znaleziono w zdaniu')  #TODO nie działa, wyświetla dla każdego słowa a nie tylko tych podanych
        print(f'indeks tego słowa to {sentence_list.index(i)}')
        list_of_words.append(i)
    else:
        continue

if not list_of_words:
    print('żadne z tych słów nie znalazło się w zdaniu')

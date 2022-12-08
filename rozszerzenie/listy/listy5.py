# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), a
# następnie korzystając z metod operujących na listach, program powinien:
# • podawać liczbę wyrazów w zdaniu
# • podawać wyrazy, które rozpoczynają się wielką literą, jeśli takie są, jeśli nie, również to zgłosić
# • sprawdzać i podawać, czy lista zawiera: „i”, „w”, „na”, „pod”, „dla”. Jeśli tak, to które są to wyrazy
# i jakie są ich indeksy na liście. Jeśli żaden z poszukiwanych wyrazów w zdaniu nie występuje program
# również powinien o tym informować
# • posortować wyrazy ze zdania alfabetycznie i wydrukować je w zmienionej kolejności.
big_letters = []
list_of_words = []
special_words = ['i', 'na', 'pod', 'dla', 'w']
forbidden_signs = ['?', '!', ',', '.', ':', ';']

sentence = input('wpisz zdanie: ')

for i in forbidden_signs:
    sentence.replace(i, ' ')
list_ = sentence.split(' ')

print(f'liczba wyrazów w zdaniu to {len(list_)}')

for element in list_:
    if  str.istitle(element):
        big_letters.append(element)
    else:
        continue
if big_letters:
    print('te wyrazy zaczynają się dużą literą:')
    for word in big_letters:
        print(' '.join(big_letters))
else:
    print("zaden wyraz nie zaczyna sie dużą literą")

for element in list_:
    if element in special_words:
        print(f'{element} znaleziono w zdaniu')
        print(f'indeks tego słowa to {list_.index(element)}')
        list_of_words.append(i)


if not list_of_words:
    print('żadne z tych słów nie znalazło się w zdaniu')

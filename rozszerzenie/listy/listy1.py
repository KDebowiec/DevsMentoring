# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), następnie:
# korzystając z metod operujących na listach, podaj wyrazy ze zdania w odwrotnej kolejności.
forbidden_signs = ['?', '!', ',', '.', ':', ';']
sentence = input('wprowadż zdanie: ')
for i in forbidden_signs:
    sentence.replace(i, ' ')

list_ = sentence.split(' ')
list_.reverse()
print('reversed sentence: ', list_)


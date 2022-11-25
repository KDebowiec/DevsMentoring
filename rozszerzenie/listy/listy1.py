# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), następnie:
# korzystając z metod operujących na listach, podaj wyrazy ze zdania w odwrotnej kolejności.
import re
sentence = None
new_text = None
first_list = []


sentence = input('wprowadż zdanie: ')
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
first_list = new_text.split()
first_list.reverse()
print('reversed sentence: ', first_list)
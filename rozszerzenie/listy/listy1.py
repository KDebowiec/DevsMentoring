# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), następnie:
# korzystając z metod operujących na listach, podaj wyrazy ze zdania w odwrotnej kolejności.
import re
sentence = None
new_text = None
first_list = []


sentence = input('wprowadż zdanie: ')

new_text = re.sub(r"[^a-zA-Z0-9 ]", "", sentence)
first_list = new_text.split()
first_list.reverse()
print('reversed sentence: ', first_list)
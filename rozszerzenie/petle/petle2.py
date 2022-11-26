# Napisz program, sprawdzający czy dany wyraz jest palindromem (jest czytany tak samo od przodu i tyłu), np. sedes, Anna.

word = input('podaj słowo, które chcesz sprawdzić: ')
reversed_word = word[::-1]

if word == reversed_word:
    print('Twoje słowo jest palindromem')
else:
    print('Niestety twoje słowo nie jest palindromem')
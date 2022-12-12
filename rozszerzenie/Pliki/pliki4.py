# Jaka jest różnica między kodowaniem UTF-8 a ASCII? Jaki byłby rezultat odczytania
# z pliku polskich liter (np. ą, ę, ć) bez zmiany sposobu formatowania danych?
#
# w UTF-8 znaki nie mają stałej długości bajtów, przyjmują 1-4 bitów, w ASCII bajty przyjmują 7 bitów.
# UTF-8 oparty na standardzie unicode może pomieścić ogromną ilość znaków, zajmuje mniej miejsca i jest polecany zawsze
# gdy dane są głównie w językach zachodnich np angielskim.
# Masz do dyspozycji plik przyklad.txt o następującej zawartości:
# |
#
# Jak możesz zauważyć, gdzieniegdzie wkradły się powtórzenia słów. Zmodyfikuj i zapisz nowy plik tak, aby się ich pozbyć.


file = open('przyklad.txt', 'r', encoding='utf-8')
text = file.readlines()
list_of_strings = []
for line in text:
    line = line.replace('\n', '')
    list_ = line.split(' ')
    list_of_strings.extend(list_)
print(list_of_strings)
# w pliku nie ma powtórzeń...
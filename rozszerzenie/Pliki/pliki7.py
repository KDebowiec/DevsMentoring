# Masz do dyspozycji plik przyklad.txt o następującej zawartości:
# |
#
# Jak możesz zauważyć, gdzieniegdzie wkradły się powtórzenia słów. Zmodyfikuj i zapisz nowy plik tak, aby się ich pozbyć.


file = open('przyklad.txt', 'r', encoding='utf-8')
text = file.readlines()
list_of_strings = []
forbidden_signs = [',', '!', ';', '\n']

for line in text:
    for i in forbidden_signs:
        line = line.replace(i, '')
    list_ = line.split(' ')
    list_of_strings.extend(list_)

for word in list_of_strings:
    if list_of_strings.count(word) > 1:
        list_of_strings.remove(word)

print(list_of_strings)
#TODO dokonczone
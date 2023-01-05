# Stwórz plik o nazwie przyklad.txt i umieść w nim następujący tekst:
# Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
# Ile cię trzeba cenić, ten tylko się dowie,
# Kto cię stracił. Dziś piękność twą w całej ozdobie
# Następnie wyświetl z pliku zawartość jego parzystych linii.
plik = open('przyklad.txt', 'r', encoding='utf-8')

for i in range(1, 3):
    if i % 2 == 1:
        line = plik.readlines()
        print(line[i])



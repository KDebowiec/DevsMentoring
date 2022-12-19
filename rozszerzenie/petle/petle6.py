# Stwórz program, który policzy częstotliwość cyfr w danej liczbie (którą poda użytkownik).
# Przykład:
# Input: 1235555
# Output:
# 1: 1
# 2: 1
# 3: 1
# 5: 4
number = input('podaj liczbę: ')
digits_in_number = []
digits_dict = {}

for i in number:
    digits_in_number.append(i)

for i in digits_in_number:
    if i not in digits_dict:
        digits_dict[i] = 1
    else:
        digits_dict[i] += 1

for key in digits_dict:
    print(f'{key} : {digits_dict[key]}')

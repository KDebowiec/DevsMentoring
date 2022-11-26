# Stwórz program, który policzy częstotliwość cyfr w danej liczbie (którą poda użytkownik).
# Przykład:
# Input: 1235555
# Output:
# 1: 1
# 2: 1
# 3: 1
# 5: 4
number = input('podaj liczbę: ')
digit = 0
digits_in_number = []
digits_set = ()

for i in number:
    digit = int(i)
    digits_in_number.append(digit)

digits_set = set(digits_in_number)

for i in digits_set:
    print(f'{i} występuje {digits_in_number.count(i)} razy')
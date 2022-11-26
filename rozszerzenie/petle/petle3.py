# W trakcie Wigilii Bożego Narodzenia, pięciu członków rodziny: Adam, Stanisław, Joanna, Kornelia i Kacper
# składają sobie życzenia. Stwórz program, który wyświetli wszystkie możliwe połączenia między członkami rodzin,
# jakie mogą zajść w trakcie składania sobie życzeń, np. Adam - Stanisław,
# Adam - Joanna, Adam - Kornelia, Adam - Kacper itd.

names_list = ['Adam', 'Stanislaw', 'Joanna', 'Kornelia', 'Kacper']
pairs = []

for i in names_list:
    for y in names_list:
        if y != i:
            pair = [y,i]
            if pair not in pairs and pair.reverse() not in pairs:
                pairs.append(pair)

for i in pairs:
    print(' '.join(i))
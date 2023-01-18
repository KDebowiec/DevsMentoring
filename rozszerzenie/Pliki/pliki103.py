# 10.3
# Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej kolumnie.
# Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128.
# Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel.
with open('pliki10_data.txt', 'r') as file:
    lines = []
    result = set()

    for i in range(2):
        line = file.readline()
        lines.append(line.split())

    while line:
        for line in file:
            for i in range(2):
                for j in range(len(lines[0]) - 1):
                    if abs(int(lines[i][j]) - int(lines[i][j + 1])) > 128:
                        result.add((i, j))
                        result.add((i, j + 1))

            for j in range(len(lines[0])):
                if abs(int(lines[0][j]) - int(lines[1][j])) > 128:
                    result.add((0, j))
                    result.add((1, j))
            lines.reverse()
            lines[1] = line.split()
        line = 0

    print(len(result))



#  METODA POBIERAJĄCA CAŁY PLIK NA RAZ
# file = open('pliki10_data.txt', 'r')
# list_of_lines = []
# list_of_pairs = []
#
#
# def lines():
#     text = file.readlines()
#     for line in text:
#         line = line.rstrip()
#         list_ = line.split(' ')
#         numbers = []
#         for element in list_:
#             element = int(element)
#             numbers.append(element)
#         list_of_lines.append(numbers)
#     return list_of_lines
#
#
# def contrast_in_line(list_of_lines):
#     for line in range(200):
#         for element in range(319):
#             if abs(list_of_lines[line][element] - list_of_lines[line][element + 1]) > 128:
#                 if [line, element] not in list_of_pairs:
#                     list_of_pairs.append([line, element])
#                 if [line, element + 1] not in list_of_pairs:
#                     list_of_pairs.append([line, element + 1])
#
#
# def contrasting_in_column(list_of_lines):
#     for line in range(199):
#         for element in range(320):
#             if abs(list_of_lines[line][element] - list_of_lines[line + 1][element]) > 128:
#                 if [line, element] not in list_of_pairs:
#                     list_of_pairs.append([line, element])
#                 if [line + 1, element] not in list_of_pairs:
#                     list_of_pairs.append([line + 1, element])
#
#
# lines()
# list_of_lines = lines()
# contrast_in_line(list_of_lines)
# contrasting_in_column(list_of_lines)
# result = len(list_of_pairs)
# print(f'wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel jest'
#       f' {result}')
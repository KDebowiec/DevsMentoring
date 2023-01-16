# 10.3
# Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej kolumnie.
# Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128.
# Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel.


"""
file.readline() => zwraca linie, gdy koniec pliku, pusty string.
petla while => dopuki nie skonczy sie plik
wyciagać 3 linie z pliku
"""

# Karolowi wyszło 753

lines_to_check = [None, None]
amount_of_contrast_number = 0

"""
lines_to_check = [
    [5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4],
]
"""

def check_lines(lines):
    amount_of_contrast_number = 0
    line_length = len(lines[0])

    for i in range(line_length):
        cursor = int(lines[0][i])

        if i < line_length - 1:
            is_next_contrast = abs(cursor - int(lines[0][i+1])) > 128
        else:
            is_next_contrast = False

        if i > 0:
            is_prev_contrast = abs(cursor - int(lines[0][i-1])) > 128
        else:
            is_prev_contrast = False

        is_below_contrast = abs(cursor - int(lines[1][i])) > 128

        if is_next_contrast or is_prev_contrast or is_below_contrast:
            amount_of_contrast_number += 1

        cursor = int(lines[1][i])

        if i < line_length - 1:
            is_next_contrast = abs(cursor - int(lines[1][i+1])) > 128
        else:
            is_next_contrast = False

        if i > 0:
            is_prev_contrast = abs(cursor - int(lines[1][i-1])) > 128
        else:
            is_prev_contrast = False

        is_above_contrast = abs(cursor - int(lines[0][i])) > 128

        if is_next_contrast or is_prev_contrast or is_above_contrast:
            amount_of_contrast_number += 1

    return amount_of_contrast_number

def change_lines(file, present_lines):
    present_lines.pop(0)

    present_lines.insert(1, file.readline().split())

    return present_lines


with open("pliki10_data.txt", "r") as file:
    for i in range(200):
        lines_to_check = [file.readline().split(), file.readline().split()]

        to_add = check_lines(lines_to_check)
        amount_of_contrast_number += to_add
        lines_to_check = change_lines(file, lines_to_check)


print(amount_of_contrast_number)


# while any(lines_to_check):
#     with open("pliki10_data.txt", "r") as file:




# with open("pliki10_data.txt", "r") as file:
#     ...



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
#
# 10.2
# Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetrii.
# Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony przyjmuje tę samą wartość,
# co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320.
file = open('pliki10_data.txt', 'r')
list_of_lines = []
# text[::-1]


def lines():
    text = file.readlines()
    for line in text:
        line = line.replace('\n', '')
        list_ = line.split(' ')
        list_of_lines.append(list_)
    return list_of_lines


def axis_of_symmetry(list_of_lines):
    lines_to_delete = []
    for line in list_of_lines:
        if line != line[::-1]:
            lines_to_delete.append(line)
    return len(lines_to_delete)


lines()
list_of_lines = lines()
axis_of_symmetry(list_of_lines)

print(f'najmniejsza liczba wierszy, które należy usunąć wynosi {axis_of_symmetry(list_of_lines)}')
# 10.2
# Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetrii.
# Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony przyjmuje tę samą wartość,
# co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320.


file = 'pliki10_data.txt'

def axis_of_symmetry(file_name):
    to_delete = 0

    with open(file_name, 'r') as file:
        for line in file:
            nums = line.split()

            if nums != nums[::-1]:
                to_delete += 1
    return to_delete

    # lines_to_delete = []
    # for line in list_of_lines:
    #     if line != line[::-1]:
    #         lines_to_delete.append(line)
    # return len(lines_to_delete)


# lines()
# list_of_lines = lines()
number_of_rows_to_delete = axis_of_symmetry(file)

print(f'najmniejsza liczba wierszy, które należy usunąć wynosi {number_of_rows_to_delete}')

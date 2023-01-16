with open('pliki10_data.txt', 'r') as file:
    lines = []
    second_line = []
    list_of_contrasting_pixels = []
    line = 1

    while line:
        for line in file:
            for i in range(1):
                lines.append(line.split())
                line = file.readline()
                lines.append(line.split())
                second_line.append(line.split())

            for line in range(2):
                for element in range(len(lines[line]) - 1):
                    if abs(int(lines[line][element]) - int(lines[line][element + 1])) > 128:
                        if [line, element] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line, element])
                        if [line, element + 1] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line, element + 1])

            for line in range(1):
                for element in range(len(lines[line])):
                    if abs(int(lines[line][element]) - int(lines[line + 1][element])) > 128:
                        if [line, element] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line, element])
                        if [line + 1, element] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line + 1, element])

            for line in range(2):
                for element in range(len(lines[line]) - 1):
                    if abs(int(lines[line][element]) - int(lines[line][element + 1])) > 128:
                        if [line, element] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line, element])
                        if [line, element + 1] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line, element + 1])

            for line in range(1):
                for element in range(len(lines[line])):
                    if abs(int(lines[line][element]) - int(lines[line + 1][element])) > 128:
                        if [line, element] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line, element])
                        if [line + 1, element] not in list_of_contrasting_pixels:
                            list_of_contrasting_pixels.append([line + 1, element])

            lines = []
            second_line = []

        break
    print(len(list_of_contrasting_pixels))
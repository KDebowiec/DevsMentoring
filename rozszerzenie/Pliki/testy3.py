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

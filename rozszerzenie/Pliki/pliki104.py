# Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie obrazka),
# złożonej z pikseli tej samej jasności.
with open('pliki10_data.txt', 'r') as file:
    lines = []
    longest_line = 0
    current_line_length = 0

    for i in range(2):
        line = file.readline()
        lines.append(line.split())

    while line:
        for line in file:
            for j in range(len(lines[0])):
                if lines[0][j] == lines[1][j]:
                    current_line_length += 1
                    lines.reverse()
                    line = file.readline()
                    lines[1] = line.split()
                elif longest_line < current_line_length:
                    longest_line = current_line_length
                    current_line_length = 1
                elif longest_line > current_line_length:
                    current_line_length = 1
            lines.reverse()
            lines[1] = line.split()

        line = 0
    print(longest_line)

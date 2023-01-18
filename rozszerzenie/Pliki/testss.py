file = open('pliki10_data.txt', 'r')
lines = []
check = []

for i in range(2):
    line = file.readline()
    lines.append(line.split())


while line:
    for line in file:
        check.append(lines)
        lines.reverse()
        lines[1] = line.split()
    line = 0

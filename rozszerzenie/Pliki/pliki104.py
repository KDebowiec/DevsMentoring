# Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie obrazka),
# złożonej z pikseli tej samej jasności.
with open('pliki10_data.txt', 'r') as file:
    list_of_lines = []


    def lines():
        text = file.readlines()
        for line in text:
            line = line.rstrip()
            list_ = line.split(' ')
            numbers = []
            for element in list_:
                element = int(element)
                numbers.append(element)
            list_of_lines.append(numbers)
        return list_of_lines


    def longest_vertical_line(list_of_lines):
        longest_line = 0
        for col in range(320):
            current_line_length = 1
            for row in range(1, 200):
                if list_of_lines[row][col] == list_of_lines[row - 1][col]:
                    current_line_length += 1
                else:
                    longest_line = max(longest_line, current_line_length)
                    current_line_length = 1

            longest_line = max(longest_line, current_line_length)
        print(longest_line)
        return longest_line


    lines()
    longest_vertical_line(list_of_lines)
    file.close()

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
        current_line_length = 1
        for row in range(200):
            for col in range(320):
                if list_of_lines[row][col] == list_of_lines[row - 1][col]:
                    current_line_length += 1
                elif longest_line == current_line_length:
                    current_line_length = 1
                elif longest_line < current_line_length:
                    longest_line = current_line_length
                elif longest_line > current_line_length:
                    current_line_length = 1

        print(longest_line)
        return longest_line


    lines()
    longest_vertical_line(list_of_lines)
    file.close()

# for i in range(len(lines)):
#     for j in range(len(lines[0])):
#         if lines[i][j] == lines[i+1][j]:
#             current_line_length += 1
#         elif longest_line < current_line_length:
#             longest_line = current_line_length
#             current_line_length = 1
#         elif longest_line > current_line_length:
#             current_line_length = 1

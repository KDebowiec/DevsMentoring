# Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie obrazka),
# złożonej z pikseli tej samej jasności.
file = open('pliki10_data.txt', 'r')
list_of_lines = []
verticals_list = []


def lines():
    text = file.readlines()
    for line in text:
        line = line.replace('\n', '')
        list_ = line.split(' ')
        numbers = []
        for element in list_:
            element = int(element)
            numbers.append(element)
        list_of_lines.append(numbers)
    return list_of_lines


def contrasting_in_column(list_of_lines):
    previous_pixel_brightness = None
    current_length = 0
    max_length = 0
    for line in range(199):
        for pixel_brightness in range(320):
            if pixel_brightness == previous_pixel_brightness:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
                previous_pixel_brightness = pixel_brightness
    max_length = max(max_length, current_length)
    print(max_length)


contrasting_in_column(list_of_lines)
            # if abs(list_of_lines[line][element] - list_of_lines[line + 1][element]) > 128:
            #     if [line, element] not in list_of_pairs:
            #         list_of_pairs.append([line, element])
            #     if [line + 1, element] not in list_of_pairs:
            #         list_of_pairs.append([line + 1, element])
#TODO problem error not found
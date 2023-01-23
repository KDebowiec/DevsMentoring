# 10.3
# Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej kolumnie.
# Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128.
# Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel.
# for nums in text:
#     numbers.append(eval(nums.replace(" ", ",")))

# numbers = [
#     (22, 11, 19, 18, 24, 26, 204, 14, 21, 19, 25, 13, 20, 22, 15, 24, 24, 26, 22, 23, 18, 15, 15, 26, 24,  20, 17, 20),
#     (15, 24, 23, 14, 18, 16,  14, 15, 26, 22, 22, 26, 23, 12, 12, 12, 24, 16, 27, 27, 25, 12, 18, 15, 20, 201, 22, 20)
# #     0,  1,  2,  3,  4,  5,   6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,  25, 26, 27
# ]
file = open('pliki10_data.txt', 'r')
lines = []


def liness():
    text = file.readlines()
    for line in text:
        line = line.rstrip()
        list_ = line.split(' ')
        lines.append(list_)
    return lines


def check_lines(lines):
    amount_of_contrast_number = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            cursor = int(lines[i][j])

            if j > 0:
                prev_num = int(lines[i][j - 1])

                if abs(cursor - prev_num) > 128:
                    amount_of_contrast_number += 1
                    continue

            if j < (len(lines[i]) - 1):
                next_num = int(lines[i][j + 1])

                if abs(cursor - next_num) > 128:
                    amount_of_contrast_number += 1
                    continue

            if i > 0:
                above_num = int(lines[i-1][j])

                if abs(cursor - above_num) > 128:
                    amount_of_contrast_number += 1
                    continue

            if i < len(lines) - 1:
                below_num = int(lines[i+1][j])

                if abs(cursor - below_num) > 128:
                    amount_of_contrast_number += 1
                    continue
    print(amount_of_contrast_number)


liness()
check_lines(lines)
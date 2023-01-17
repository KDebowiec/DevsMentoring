# 10.3
# Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej kolumnie.
# Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128.
# Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel.


import time


text = """
22 11 19 18 24 26 24 14 21 19 25 13 20 22 15 24 24 26 22 23 18 15 15 26 24 20 17 20 25 21 11 17 15 24 26 16 13 26 26 26 20 20 14 13 24 16 24 17 18 24 14 13 23 18 18 25 25 13 20 13 11 21 17 18 15 14 19 12 17 15 25 24 15 21 21 19 19 23 12 17 12 14 20 21 14 15 20 25 19 13 11 16 13 25 13 12 17 25 18 23 19 12 15 18 14 13 14 19 20 14 18 25 11 19 18 22 24 17 23 16 13 11 23 16 26 14 11 22 26 23 18 11 24 20 11 17 21 16 11 13 17 13 25 19 26 24 22 15 15 20 16 22 23 13 12 11 25 14 18 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 26 19 25 13 17 13 11 16 21 17 11 20 24 11 18 23 26 22 11 14 26 16 23 11 13 16 23 17 24 22 18 19 11 25 18 14 20 19 14 13 14 18 15 12 19 23 18 25 17 12 13 25 13 16 11 13 19 25 20 15 14 21 20 14 12 17 12 23 19 19 21 21 15 24 25 15 17 12 19 14 15 18 17 21 11 13 20 13 25 25 18 18 23 13 14 24 18 17 24 16 24 13 14 20 20 26 26 26 13 16 26 24 15 17 11 21 25 20 17 20 24 26 15 15 18 23 22 26 24 24 15 22 20 13 25 19 21 14 24 26 24 23 19 11 22
15 24 23 14 18 16 14 15 26 22 22 26 23 12 12 12 24 16 27 27 25 12 18 15 20 201 22 20 15 14 21 20 22 23 22 25 20 12 13 18 14 23 13 19 19 16 21 23 16 19 26 25 20 26 202 14 13 16 16 21 21 17 15 17 14 17 24 20 23 12 17 19 15 19 13 15 18 27 18 26 12 27 13 23 22 25 20 20 20 18 17 19 15 26 12 12 16 20 19 24 12 22 15 27 27 22 27 14 16 20 22 13 202 15 16 22 20 16 18 23 17 17 25 20 22 14 18 14 22 17 27 15 12 26 26 14 22 20 20 26 24 24 23 24 24 19 19 12 20 18 24 13 25 19 19 24 24 25 208 23 23 208 25 24 24 19 19 25 13 24 18 20 12 19 19 24 24 23 24 24 26 20 20 22 14 26 26 12 15 27 17 22 14 18 14 22 20 25 17 17 23 18 16 20 22 16 15 202 13 22 20 16 14 27 22 27 27 15 22 12 24 19 20 16 12 12 26 15 19 17 18 20 20 20 25 22 23 13 27 12 26 18 27 18 15 13 19 15 19 17 12 23 20 24 17 14 17 15 17 21 21 16 16 13 14 202 26 20 25 26 19 16 23 21 16 19 19 13 23 14 18 13 12 20 25 22 23 22 20 21 14 15 20 22 201 20 15 18 12 25 27 27 16 24 12 12 12 23 26 22 22 26 15 14 16 18 14 23 24 15
25 25 21 27 13 20 15 16 20 14 16 23 26 25 24 18 24 22 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 15 16 25 26 21 17 27 28 27 20 27 20 13 13 25 15 19 24 17 13 22 22 24 24 16 27 28 14 13 24 19 24 26 17 24 13 14 15 15 27 18 20 21 25 18 27 20 24 22 13 17 28 23 27 23 16 22 14 16 13 15 23 20 21 23 27 24 16 27 17 28 22 20 18 17 17 21 21 28 16 15 26 20 22 18 23 25 16 19 16 15 15 14 19 21 22 13 24 22 22 27 17 27 25 27 24 14 22 16 23 14 23 21 20 14 14 20 21 23 14 23 16 22 14 24 27 25 27 17 27 22 22 24 13 22 21 19 14 15 15 16 19 16 25 23 18 22 20 26 15 16 28 21 21 17 17 18 20 22 28 17 27 16 24 27 23 21 20 23 15 13 16 14 22 16 23 27 23 28 17 13 22 24 20 27 18 25 21 20 18 27 15 15 14 13 24 17 26 24 19 24 13 14 28 27 16 24 24 22 22 13 17 24 19 15 25 13 13 20 27 20 27 28 27 17 21 26 25 16 15 23 25 22 17 25 17 21 21 18 22 19 15 28 24 14 21 20 20 15 21 19 17 19 20 27 26 16 22 24 18 24 25 26 23 16 14 20 16 15 20 13 27 21 25 25
"""

text = text.strip().split('\n')

numbers = []
# for nums in text:
#     numbers.append(eval(nums.replace(" ", ",")))

# numbers = [
#     (22, 11, 19, 18, 24, 26, 204, 14, 21, 19, 25, 13, 20, 22, 15, 24, 24, 26, 22, 23, 18, 15, 15, 26, 24,  20, 17, 20),
#     (15, 24, 23, 14, 18, 16,  14, 15, 26, 22, 22, 26, 23, 12, 12, 12, 24, 16, 27, 27, 25, 12, 18, 15, 20, 201, 22, 20)
# #     0,  1,  2,  3,  4,  5,   6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,  25, 26, 27
# ]

file = open('pliki10_data.txt', 'r')
for line in file:
    numbers.append(line.split())
file.close()


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
    return amount_of_contrast_number


def mod_found_by_karol():
    tab = numbers
    result = set()

    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if j < len(tab[0]) - 1:
                if abs(int(tab[i][j]) - int(tab[i][j + 1])) > 128:
                    result.add((i, j))
                    result.add((i, j + 1))
            if i < len(tab) - 1:
                if abs(int(tab[i][j]) - int(tab[i + 1][j])) > 128:
                    result.add((i, j))
                    result.add((i + 1, j))

    return len(result)


def org_found_by_karol():
    tab = numbers
    result = []

    for i in range(200):
        for j in range(319):
            if abs(int(tab[i][j]) - int(tab[i][j + 1])) > 128:
                if [i, j] not in result:
                    result.append([i, j])
                if [i, j + 1] not in result:
                    result.append([i, j + 1])

    for i in range(199):
        for j in range(320):
            if abs(int(tab[i][j]) - int(tab[i + 1][j])) > 128:
                if [i, j] not in result:
                    result.append([i, j])
                if [i + 1, j] not in result:
                    result.append([i + 1, j])
    return len(result)


start = time.perf_counter_ns()
result = check_lines(numbers)
print("Benchmark result:", (time.perf_counter_ns() - start))
print("Mine result:", result)

print()

start = time.perf_counter_ns()
result = mod_found_by_karol()
print("Benchmark result:", (time.perf_counter_ns() - start))
print("Mod found by Karol result:", result)

print()

start = time.perf_counter_ns()
result = org_found_by_karol()
print("Benchmark result:", (time.perf_counter_ns() - start))
print("Org found by Karol result:", result)

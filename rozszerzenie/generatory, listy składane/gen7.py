# Mając do dyspozycji poniższą listę trójwymiarową:
# three_d = [
# [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
# [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
# ]
# przefiltruj ją tak, by znalazły się tylko te najbardziej wewnętrzne listy, których ilość elementów przekracza 4.
#
# Wynikiem powinna być lista:
# [[0, -1, -2, -3, -4, -5, -6], [1, 10, 15, 1, 20, 20, 20], [-15, -13, 14, 20, -1]]
three_d = [
    [
        [1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]
    ],
    [
        [1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]
    ]
]
filtered_list = [i for row in three_d for i in row if len(i) > 4]

# for sublist in three_d:
#     for subsub in sublist:
#         if len(subsub) > 4:
#             filtered_list.append(subsub)

print(filtered_list)
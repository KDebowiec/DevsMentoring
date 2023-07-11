# Mając do dyspozycji poniższą listę liczb całkowitych:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Stwórz listę new_nums, która będzie zawierała kwadraty powyższych liczb, ale tylko takich, które są parzyste. Wykorzystaj lambdy.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new = list(map(lambda x: x**2, nums))
new_nums = list(filter(lambda x: x % 2 == 0, new))
print(new_nums)

# Napisz program, który obliczy sumę trzech list o tej samej długości i zwróci wynik jednej konkretnej liczby. Wykorzystaj map() oraz lambdę.
from functools import reduce
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]


nums = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))
result = reduce(lambda x, y: x + y, nums)

nums = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))
final = list(map(lambda x, y: x + y, nums))

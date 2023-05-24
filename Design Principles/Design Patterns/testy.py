# class Solution:
#     def removeDuplicates(self, nums):
#         k = 0
#
#         list_of_recurring = []
#         for element in nums:
#             if element not in list_of_recurring:
#                 list_of_recurring.append(element)
#                 k += 1
#             else:
#                 nums.pop(nums.index(element))
#                 nums.insert(nums.index(element), '_')
#
#         for element in nums:
#             if element == '_':
#                 nums.pop(nums.index(element))
#                 nums.extend(['_'])
#
#         print(nums)
#         return k
#
#
# solution = Solution()
# solution.removeDuplicates([1, 1, 2, 2, 2, 3, 4])


nums = [3, 3]
target = 3

list_of_index = []
for i in nums:
    different = target - i
    for y in range(1, len(nums)):
        if nums[y] == different:
            if y != nums.index(i):
                if len(list_of_index) != 2:
                    list_of_index.extend([nums.index(i), y])

print(list_of_index)
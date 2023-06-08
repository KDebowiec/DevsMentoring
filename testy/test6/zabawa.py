class Solution:
    def twoSum(self, nums, target: int):
        list_of_index = []
        while len(nums) != 2:
            for i in nums:
                if i < target:
                    list_of_index.append(nums.index(i))
                    different = target - i
                for y in nums:
                    if y == different and nums.index(y) != nums.index(i):
                        list_of_index.append(nums.index(y))

        print(list_of_index)


solution = Solution()
solution.twoSum([2, 7, 11, 15], 9)

class Solution:
    def twoSum(self, nums, target: int):
        for i in nums:
            for y in range(len(nums)):
                if nums[i] + nums[y] == target:
                    print([i, y])
                    return [i, y]


solution = Solution()
solution.twoSum([1, 2, 4], 5)

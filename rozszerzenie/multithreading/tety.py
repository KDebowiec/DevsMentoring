# class Solution:
#     def twoSum(self, nums, target: int):
#         for i in nums:
#             for y in range(len(nums)):
#                 if nums[i] + nums[y] == target:
#                     print([i, y])
#                     return [i, y]
#
#
# solution = Solution()
# solution.twoSum([1, 2, 4], 5)
import re
# class Solution:
#     def isValid(self, s):
#         for i in s:
#             print(s[s.index(i)])
#             print(s[len(s) - s.index(i) - 1])
#             if s[s.index(i)] == s[len(s) - s.index(i) - 1]:
#                 print('true')
#                 return True
#             elif s[s.index(i)] == s[s.index(i) + 1]:
#                 print('true')
#                 return True
#             else:
#                 print('false')
#                 return False
#
#
# solution = Solution()
# solution.isValid('{[]}')
#
class Solution(object):
    def isValid(self, s):
        stack = []
        for element in s:
            if element in '([{':
                stack.append(element)
            else:
                if not stack or \
                    (element == ')' and stack[-1] != '(') or \
                    (element == '}' and stack[-1] != '{') or \
                    (element == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack

solution = Solution()
solution.isValid('[{}{}]')

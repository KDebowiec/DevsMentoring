class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            print(haystack.index(needle))
        else:
            return -1


solution = Solution()
solution.strStr('butsad', 'sad')
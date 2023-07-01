class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        j = 0 
        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                j += 1
            else:
                j = 0
            if j == len_needle:
                return i-(j-1)
        return -1
                
                
solution = Solution().strStr("leetcode", "leeto")

print(solution)
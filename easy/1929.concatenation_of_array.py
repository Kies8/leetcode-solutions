from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

nums = [1,2,3]

solution = Solution().getConcatenation(nums)
print(solution)
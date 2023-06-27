from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans: List[int] = [0] * len(nums)
        for i, num in enumerate(nums):
            ans[i] = nums[num]
        return ans
        
        
nums = [0,2,1,5,3,4]        

solution = Solution().buildArray(nums)
print(solution)

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
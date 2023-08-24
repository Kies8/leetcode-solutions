from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        obj = {}
        for num in nums:
            if num in obj:
                obj[num] += 1
            else:
                obj[num] = 1

        for key, value in obj.items():
            if value > (len(nums) / 2):
                return key

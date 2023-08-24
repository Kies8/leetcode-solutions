from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         obj = {}
#         for num in nums:
#             if num in obj:
#                 obj[num] += 1
#             else:
#                 obj[num] = 1

#         for key, value in obj.items():
#             if value > (len(nums) / 2):
#                 return key


# Optimized Solution Boyer-Moore
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

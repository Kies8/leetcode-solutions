from typing import List

class Solution:
    def quicksort(self, arr) -> List[int]:
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot] 

        return self.quicksort(left) + mid + self.quicksort(right)

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = self.quicksort(nums)
        mapping = {}
        
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in mapping:
                mapping[sorted_nums[i]] = i
                
        return [mapping[num] for num in nums]

nums = [8,1,2,2,3]  
solution = Solution().smallerNumbersThanCurrent(nums)
print(solution)
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans: List[bool] = []
        max_num:int = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_num:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
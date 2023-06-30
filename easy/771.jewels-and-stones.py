class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewels_arr = list(jewels)

        for stone in stones:
            if stone in jewels_arr:
                ans +=1
        return ans
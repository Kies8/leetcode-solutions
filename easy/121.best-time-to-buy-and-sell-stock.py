class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = float("inf")
        profit = 0

        for price in prices:
            if price < stock:
                stock = price
            else:
                new_profit = price - stock
                profit = new_profit if profit < new_profit else profit

        return profit

import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = 0

        for i in range(len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]

            curr_profit = prices[i] - min_price

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit
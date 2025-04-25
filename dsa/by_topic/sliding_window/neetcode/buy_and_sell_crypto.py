"""
https://neetcode.io/problems/buy-and-sell-crypto
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        p1, p2, max_profit = 0, 1, 0

        while p2 < len(prices):
            max_profit  = max(max_profit, prices[p2]-prices[p1])
            if prices[p2] < prices[p1]:
                p1 = p2
            p2+=1

        return max_profit





class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_count = 0
        for i in range(len(prices)-1):
            x = max(prices[i+1:]) -prices[i]
            if x > max_count:
                max_count = x
        return max_count
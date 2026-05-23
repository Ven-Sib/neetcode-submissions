class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n-1):
            profit = max(prices[i+1:])-prices[i]
            max_profit = max(max_profit, profit)
        return max_profit

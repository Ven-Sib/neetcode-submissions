class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices)-1):
            profit = max(prices[i+1:])- prices[i]
            max_prof = max(profit, max_prof)
        
        return max_prof
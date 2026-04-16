class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices)-1):
            profit = max(prices[i+1:])- prices[i]
            if profit > max_prof:
                max_prof = profit
        
        return max_prof
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold, cash = float('-inf'), 0
        for p in prices:
            hold = max(hold, cash - p)   # keep holding, or buy today
            cash = max(cash, hold + p)   # stay in cash, or sell today
        return cash
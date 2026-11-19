class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_Sum = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(currSum,0)
            currSum += n
            max_Sum = max(max_Sum, currSum)
        
        return max_Sum
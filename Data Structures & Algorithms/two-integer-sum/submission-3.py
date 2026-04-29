class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            cul = target-nums[i]
            if cul in dict1:
                return [dict1[cul], i]
            dict1[nums[i]] = i
        return 

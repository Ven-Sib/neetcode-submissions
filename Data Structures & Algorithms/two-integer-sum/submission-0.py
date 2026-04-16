class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dict1:
                return [dict1[x],i]
            dict1[nums[i]] = i
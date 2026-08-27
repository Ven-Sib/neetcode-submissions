class Solution:
    def findMin(self, nums: List[int]) -> int:
        minim = float("inf")
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2
            minim = min(minim, nums[mid])
            if nums[mid] >= nums[l]:
                minim = min(minim, nums[l])
                l = mid + 1
            else:
                r = mid -1
        return minim


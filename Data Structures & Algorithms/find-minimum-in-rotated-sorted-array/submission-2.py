class Solution:
    def findMin(self, nums: List[int]) -> int:
        minim = float("inf")
        n = len(nums)
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right)//2
            minim = min(minim, nums[mid])
            if nums[mid] >= nums[left]:
                minim = min(minim, nums[left])
                left += 1
            else:
                right -= 1
        return minim
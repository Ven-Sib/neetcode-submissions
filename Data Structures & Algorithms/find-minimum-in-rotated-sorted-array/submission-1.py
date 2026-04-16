class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        minim = float('inf')
        while left <= right:
            mid = (right+left)//2
            minim = min(minim, nums[mid])
            if nums[mid] >= nums[left]:
                minim = min(minim, nums[left])
                left = mid + 1
            else:
                right = mid-1
            
            print(minim)
        return minim
            
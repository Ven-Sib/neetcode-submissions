class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                a = nums[i] 
                b = nums[l] 
                c = nums[r]
                total = a+b+c
                if total == 0:
                    res.append([a, b, c])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total <0:
                    l += 1
                else:
                    r -= 1
        return res
                    

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, n in enumerate(nums):
            if i > far:          # index i is unreachable
                return False
            far = max(far, i + n)
        return True
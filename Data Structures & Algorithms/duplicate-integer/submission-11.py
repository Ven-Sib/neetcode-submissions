class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = {}

        for i in nums:
            numset[i] = 1 + numset.get(i,0)
            if numset[i] > 1:
                return True
        return False



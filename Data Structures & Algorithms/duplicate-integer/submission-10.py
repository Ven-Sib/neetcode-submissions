class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numseen = set()

        for num in nums:
            if num in numseen:
                return True
            else:
                numseen.add(num)
        return False


            
        
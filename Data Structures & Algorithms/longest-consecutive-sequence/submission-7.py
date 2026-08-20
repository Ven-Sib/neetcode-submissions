class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initiate a set to store the numbers uniquely
        #  initiate a max_length var to store the max value
        #  initiate a length var to store current consec seq
        #  increment  lenth when ever we find an item 1 greater
        # set length to zero when a new seq starts 
        # initiate a mx_length var to store 

        numSet = set(nums)
        max_length = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                max_length = max(max_length, length)
        return max_length
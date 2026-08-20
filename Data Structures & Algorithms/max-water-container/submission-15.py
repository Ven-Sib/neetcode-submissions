class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #  initiate the left and right pointer to keep track of the length between 2 bars and use the minimum bar of the two as the cutting height since water cannot go over that height(spill) 
        n = len(heights)
        l = 0
        r = n-1
        max_area = 0

        while l < r:
            # determine the area covered at most by the smallest of heights
            area = (r-l)*min(heights[l], heights[r])
            # move to the right if height on the left is less than height on the right
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            #  return the maximum area
            max_area = max(max_area, area)
        return max_area
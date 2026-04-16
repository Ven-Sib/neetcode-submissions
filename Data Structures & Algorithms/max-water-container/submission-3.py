class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_h = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                x = (j-i)*(min(heights[i], heights[j]))
                if x > max_h:
                    max_h = x
        return max_h
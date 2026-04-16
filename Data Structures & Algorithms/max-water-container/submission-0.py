class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_wat = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                x = (j-i)*(min(heights[i], heights[j]))
                if x > max_wat:
                    max_wat = x
        return max_wat
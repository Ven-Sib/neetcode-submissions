class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot)//2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        if not top <= bot:
            return False
        row = (top+bot)//2
        left, right = 0, len(matrix[0])
        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left += 1
            else:
                right -= 1
            
        return False



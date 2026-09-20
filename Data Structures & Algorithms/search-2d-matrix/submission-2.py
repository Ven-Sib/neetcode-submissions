class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix)-1, len(matrix[0])-1

        bot, top = ROW, 0

        while top <= bot:
            row = (top+bot)//2
            if target < matrix[row][0]:
                bot = row -1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        # if not top <= bot:
        #     return False

        row = (top+bot)//2

        l, r = 0, COL
        while l <= r:
            mid = (l+r)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
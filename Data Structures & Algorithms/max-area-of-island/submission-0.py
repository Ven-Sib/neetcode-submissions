class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Row, Col = len(grid), len(grid[0])
        path = set()

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= Row or c >= Col):
                return 0
            if grid[r][c] == 0 or (r, c) in path:
                return 0

            path.add((r,c))

            area = 1

            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        max_area  = 0
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1 and (r,c) not in path:
                    max_area = max(max_area, dfs(r,c))

        return max_area

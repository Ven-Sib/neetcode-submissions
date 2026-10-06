class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        path = set()
        y = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in path or grid[r][c] == 0:
                return 0
            path.add((r,c))
            x = 1

            x += dfs(r+1,c)
            x += dfs(r-1,c)
            x += dfs(r,c+1)
            x += dfs(r,c-1)

            return x
            

        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in path:
                    y = max(y, dfs(r,c))
                
                    

        return y

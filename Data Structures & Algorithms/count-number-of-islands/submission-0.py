class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row, Col = len(grid), len(grid[0])
        path = set()
        islands = 0
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= Row or c >= Col ):
                return 
            
             # stop if water or already visited
            if grid[r][c] == "0" or (r, c) in path:
                return
            
            path.add((r,c))
            res = (dfs(r+1, c) or dfs(r-1, c) or
            dfs(r, c+1) or dfs(r, c-1))

            return res
        
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == "1" and (r,c) not in path:
                    dfs(r,c)
                    islands += 1
        
        return islands

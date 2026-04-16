class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row, Col = len(grid), len(grid[0])
        path = set()

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= Row or c >= Col):
                return
            if grid[r][c] == "0" or (r,c) in path:
                return
            path.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        islands = 0
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == "1" and (r, c) not in path:
                    islands += 1
                    dfs(r, c)
        return islands
        
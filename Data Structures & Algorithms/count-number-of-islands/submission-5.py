class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row, Col = len(grid), len(grid[0])
        path = set()

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= Row or c >= Col):
                return False
            if grid[r][c] == "0" or (r, c) in path:
                return False

            path.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        components = 0

        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == "1" and (r,c) not in path:
                    dfs(r,c)
                    components += 1
        return components

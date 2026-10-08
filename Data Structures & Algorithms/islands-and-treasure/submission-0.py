class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
        direction = [[0,1],[0,-1],[1,0],[-1,0]]

        dist = 0
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] != 2147483647 or (row,col) in visited:
                        continue
                    
                    grid[row][col] = 1 + dist
                    q.append((row,col))
                    visited.add((row,col))

            dist += 1




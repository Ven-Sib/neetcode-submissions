class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited  = set()
        
        dist = 0
        ROW, COL = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = dr + r, dc + c
                    if row < 0 or row >=ROW or col < 0 or col >= COL or grid[row][col] == -1 or (row,col) in visited:
                        continue
                    grid[row][col]  = dist + 1
                    visited.add((row, col))
                    q.append([row,col])
                    
            dist += 1

        

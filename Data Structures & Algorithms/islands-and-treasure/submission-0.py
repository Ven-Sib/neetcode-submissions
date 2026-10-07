class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    # visited.add((r,c))

        direction = [0,1], [0,-1], [1,0], [-1,0]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] != 2147483647 or (row,col) in visited:
                        continue

        
                    grid[row][col] = dist + 1
                    q.append((row,col))
                    visited.add((row,col))
                
            dist += 1

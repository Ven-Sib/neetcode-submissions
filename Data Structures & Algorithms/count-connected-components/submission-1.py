class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize num_nodes x num_nodes matrix with 0s
        adj_matrix = [[0]*n for _ in range(n)]

        # Fill in connections
        for u, v in edges:
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1   # undirected graph (remove if directed)
        print(adj_matrix)

        x = len(adj_matrix)
        visited = set()

        def dfs(edge):
            for i in range(x):
                if i not in visited and adj_matrix[i][edge] == 1:
                    visited.add(i)
                    dfs(i)
        
        components = 0
        for i in range(x):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        return components
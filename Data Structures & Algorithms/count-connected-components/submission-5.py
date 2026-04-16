class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        list1 = [[0]*n for i in range(n)]
        for i, j in edges:
            list1[i][j] = 1
            list1[j][i] = 1
        n = len(list1)
        path = set()
        def dfs(edge):
            for i in range(n):
                if list1[i][edge] == 1 and i not in path:
                    path.add(i)
                    dfs(i)
        components = 0
        for i in range(n):
            if i not in path:
                path.add(i)
                dfs(i)
                components += 1
        return components

            
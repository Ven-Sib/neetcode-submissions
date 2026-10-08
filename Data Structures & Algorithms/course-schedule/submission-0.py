class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1 = {i:[] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            dict1[crs].append(pre)
        
        def dfs(crs):
            if dict1[crs] == []:
                return True
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in dict1[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            dict1[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
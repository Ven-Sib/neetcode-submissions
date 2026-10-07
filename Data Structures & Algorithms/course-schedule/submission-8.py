class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1 = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            dict1[crs].append(pre)
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return False
            if dict1[crs] == []:
                return True

            visit.add(crs)
            for pre in dict1[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs) 
            dict1[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
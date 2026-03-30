class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}

        for to, _from in prerequisites:
            courses[to].append(_from)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if courses[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            courses[crs] = []

            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

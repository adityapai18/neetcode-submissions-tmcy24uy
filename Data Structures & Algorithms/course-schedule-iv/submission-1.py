class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)
        
        memo = {}
        
        def dfs(u,v):
            if u == v:
                return True
            
            if (u,v) in memo: 
                return memo[(u,v)]
            
            for node in graph[u]:
                if node == u:
                    continue
                memo[(u,v)] = dfs(node,v)
                if memo[(u,v)]:
                    return True
            memo[(u,v)] = False
            return memo[(u,v)]

        res = []
        for u,v in queries:
            res.append(dfs(u,v))
        
        return res
        

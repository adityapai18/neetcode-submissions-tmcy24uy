class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, eq in enumerate(equations):
            a,b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        def dfs(src,target, visited):
            if src not in graph or target not in graph:
                return -1
            if src == target:
                return 1
            
            visited.add(src)
            for nei, weight in graph[src]:
                if nei not in visited:
                    result = dfs(nei,target,visited)
                    if result != -1:
                        return result*weight
            return -1
        
        res = []
        for query in queries:
            res.append(dfs(query[0],query[1],set()))
        
        return res
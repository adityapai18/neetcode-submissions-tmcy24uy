from collections import deque, defaultdict
import heapq
from typing import List
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(num_vertices,graph):
            indegree = [0] * num_vertices
            for u in range(num_vertices):
                for vertice in graph[u]:
                    indegree[vertice] += 1
            
            queue = deque([i for i, deg in enumerate(indegree) if deg == 0])
            topo = []

            while queue:
                u = queue.popleft()
                topo.append(u)

                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            
            if len(topo) != num_vertices:
                return False
            
            return topo
        
        res = [[0] * k for i in range(k)]

        rowgraph = [[] for _ in range(k)]
        colgraph = [[] for _ in range(k)]

        for u, v in rowConditions:
            rowgraph[u - 1].append(v - 1)
        
        for u, v in colConditions:
            colgraph[u - 1].append(v - 1)

        topo_row = topo_sort(k,rowgraph)
        topo_col = topo_sort(k,colgraph)
        if topo_row == False or topo_col == False:
            return []

        row_pos = {num: i for i, num in enumerate(topo_row)}
        col_pos = {num: i for i, num in enumerate(topo_col)}

        for i in range(k):
            res[row_pos[i]][col_pos[i]] = i + 1

        return res

if __name__ == "__main__":
    s = Solution()
    k = 3
    rowConditions = [[1,2],[3,2]]
    colConditions = [[2,1],[3,2]]
    print(s.buildMatrix(k, rowConditions, colConditions))
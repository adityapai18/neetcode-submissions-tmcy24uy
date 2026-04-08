from collections import deque, defaultdict
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node,parent):
            ht = 0
            for nei in graph[node]:
                if nei == parent:
                    continue
                ht = max(ht, 1 + dfs(nei, node))
            return ht

        minht = n
        res = []
        for i in range(n):
            ht = dfs(i,-1)
            if ht == minht:
                res.append(i)
            elif ht < minht:
                res = [i]
                minht = ht
        
        return res


        
if __name__ == "__main__":
    s = Solution()
    print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
    print(s.findMinHeightTrees(6, [[0,3],[1,3],[2,3],[4,3],[5,4]]))
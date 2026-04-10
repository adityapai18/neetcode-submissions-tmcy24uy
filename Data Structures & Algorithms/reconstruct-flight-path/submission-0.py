from collections import deque, defaultdict
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for a,b in tickets:
            graph[a].append(b)
        
        for val in graph:
            graph[val].sort(reverse=True)
        

        res = []

        def dfs(node):

            while graph[node]:
                next_dest = graph[node].pop()
                dfs(next_dest)
            
            res.append(node)
        
        dfs("JFK")

        return res[::-1]


        
        
if __name__ == "__main__":
    s = Solution()
    print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
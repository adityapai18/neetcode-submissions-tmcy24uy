from collections import deque, defaultdict
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1,N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        minHeap = [(0,0)]

        visited = set()

        while len(visited) < N:
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue

            visited.add(point)

            res+= cost
            for neicost, i in adj[point]:
                if i not in visited:
                    heapq.heappush(minHeap,[neicost, i])
        
        return res


        

if __name__ == "__main__":
    s = Solution()
    print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
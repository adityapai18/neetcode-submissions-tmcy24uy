from collections import deque, defaultdict
import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N, node = len(points), 0

        dist = [float('inf')] * N
        visit = [False] * N
        edges, res = 0 , 0

        while edges < N - 1:
            visit[node] = True
            nextNode = -1

            for i in range(N):
                if visit[i]:
                    continue
                curDist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])

                dist[i] = min(dist[i], curDist)

                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            edges+=1
            node = nextNode

        return res

        # adj = [[] for _ in range(N)]
        # for i in range(N):
        #     for j in range(i+1,N):
        #         dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        #         adj[i].append([dist, j])
        #         adj[j].append([dist, i])
        
        # res = 0
        # minHeap = [(0,0)]

        # visited = set()

        # while len(visited) < N:
        #     cost, point = heapq.heappop(minHeap)

        #     if point in visited:
        #         continue

        #     visited.add(point)

        #     res+= cost
        #     for neicost, i in adj[point]:
        #         if i not in visited:
        #             heapq.heappush(minHeap,[neicost, i])
        
        # return res


        

if __name__ == "__main__":
    s = Solution()
    print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
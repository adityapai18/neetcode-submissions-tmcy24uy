from collections import deque, defaultdict
import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0],0,0]]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        visited.add((0, 0))
        while minHeap:
            val, x, y = heapq.heappop(minHeap)

            if (x,y) == (ROWS - 1, COLS-1):
                return val

            
            for dr, dc in direction:
                newX, newY = x+dr, y+dc
                if newX <0 or newY<0 or newX>= ROWS or newY >= COLS or (newX, newY) in visited:
                    continue

                visited.add((newX,newY))

                heapq.heappush(minHeap,[max(val,grid[newX][newY]), newX, newY])

        return 0
from collections import deque, defaultdict
import heapq
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        minHeap = [[0,0,0]]
        ROWS, COLS = len(heights), len(heights[0])

        while minHeap:
            val, x, y = heapq.heappop(minHeap)
            if (x, y) in visit:
                continue
            visit.add((x,y))

            if (x,y) == (ROWS - 1, COLS - 1):
                return val
            
            for dr, dc in direction:
                newX, newY = x+dr, y+dc
                if newX<0 or newY<0 or newX >= ROWS or newY >= COLS or(newX, newY) in visit:
                    continue
                newDiff = max(val, abs(heights[newX][newY] - heights[x][y]))
                heapq.heappush(minHeap,[newDiff,newX,newY])
        
        return 0
              
if __name__ == "__main__":
    s = Solution()
    print(s.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])) # 2
    print(s.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])) # 1
    print(s.minimumEffortPath([[1,2,1],[3,8,1],[5,3,5]])) # 0
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = [[grid[0][0], 0, 0]]  # [max_elevation, r, c]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        
        # Mark the start as visited so we don't go backwards to it
        visited.add((0, 0))

        while minHeap:
            val, x, y = heapq.heappop(minHeap)

            # If we reached the bottom-right, return the max elevation seen
            if (x,y) == (ROWS-1, COLS-1):
                return val

            for dr, dc in direction:
                newX, newY = x + dr, y + dc
                
                # Check bounds and if already visited
                if newX < 0 or newY < 0 or newX >= ROWS or newY >= COLS or (newX, newY) in visited:
                    continue

                # Mark the NEIGHBOR as visited immediately so it isn't added to the heap twice
                visited.add((newX, newY))

                # Push the NEIGHBOR to the heap. 
                # The new cost is the max of our current path cost and the neighbor's height
                heapq.heappush(minHeap, [max(val, grid[newX][newY]), newX, newY])

        return 0
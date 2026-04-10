from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid) , len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
                
            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1

            res = dfs(r + 1, c)
            res += dfs(r - 1, c)
            res += dfs(r, c + 1)
            res += dfs(r, c - 1)

            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)
        
        return 0
        

                  
                 


# if __name__ == "__main__":
    # s = Solution()
    # print(s.islandPerimeter([[0, 1, 0, 0],
    #                          [1, 1, 1, 0],
    #                          [0, 1, 0, 0],
    #                          [1, 1, 0, 0]]))
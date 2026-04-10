class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # 1. BASE CASE: If we go out of bounds or hit water, that's a perimeter side!
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
            
            # 2. BASE CASE: If we hit a cell marked -1, we've already been here.
            if grid[r][c] == -1:
                return 0
            
            # 3. Mark the current cell as visited so we don't count it again
            grid[r][c] = -1
            
            # 4. Sum up the results from all 4 directions
            res = dfs(r + 1, c)
            res += dfs(r - 1, c)
            res += dfs(r, c + 1)
            res += dfs(r, c - 1)
            
            return res

        # Start DFS at the first land cell we find
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return 0
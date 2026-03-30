class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def dfs(curr):
            # Base Case: We've built a complete permutation
            if len(curr) == n:
                # We append a copy [:] because lists are passed by reference
                res.append(curr[:]) 
                return
            
            for j in range(n):
                # Skip if the number is already used in the current path
                if nums[j] in curr:
                    continue
                
                # Choose: Add the number
                curr.append(nums[j])
                
                # Explore: Move to the next level of the tree
                dfs(curr)
                
                # Un-choose: Remove the number (Backtrack)
                curr.pop()

        dfs([])
        return res
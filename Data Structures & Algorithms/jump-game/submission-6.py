class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # memo = [-1] * n
        # def dfs(i):
        #     if i == n:
        #         return True
            
        #     if i in memo:
        #         return memo[i]
            
        #     if nums[i] == 0:
        #         return False

        #     end = min(len(nums) - i, nums[i])

        #     for j in range(i+1, end):
        #         if dfs(j):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False
        
        # return dfs(0)
        

        n = len(nums)
        goal = n -1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, brought):
            if i == len(prices):
                return 0
            
            if (i, brought) in memo:
                return memo[(i, brought)]
            
            res = dfs(i+1, brought)

            if brought:
                res = max(res, prices[i] + dfs(i+1, False))
            else:
                res = max(res, dfs(i+1, True) - prices[i])
            
            memo[(i, brought)] = res
            return res
        
        return dfs(0, False)
        
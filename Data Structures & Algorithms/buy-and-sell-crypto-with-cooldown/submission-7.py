class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        memo = {}
        
        def dfs(i, buy):
            if i >= n:
                return 0
            
            if (i,buy) in memo:
                return memo[(i,buy)]
                
            cooldown = dfs(i+1 , buy)

            
            if buy:
                buying = dfs(i+1, not buy)- prices[i]
                memo[(i,buy)] =  max(buying, cooldown)

            else:
                sell = dfs(i+2, not buy) + prices[i]
                memo[(i,buy)] =  max(sell, cooldown)

            return memo[(i,buy)]
        return dfs(0, True)
                
            

            

        
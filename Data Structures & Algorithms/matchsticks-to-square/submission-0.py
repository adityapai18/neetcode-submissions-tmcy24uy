from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
            if len(matchsticks) < 4:
                return False
            total_sum = sum(matchsticks)
            if total_sum  % 4 != 0:
                return False
            
            n = len(matchsticks)
            side_length = total_sum // 4

            if side_length < max(matchsticks):
                return False
            
            matchsticks.sort(reverse=True)
            sides = [0] * 4

            def dfs(idx):
                if idx == len(matchsticks):
                    return True
                
                for i in range(4):
                     if sides[i] + matchsticks[idx] <= side_length:
                          sides[i] += matchsticks[idx]

                          if dfs(idx+1):
                               return True
                          
                          sides[i] -= matchsticks[idx]

                
                return False
            
            return dfs(0)
            
if __name__ == "__main__":
    s = Solution()
    print(s.makesquare([1,5,6,3]))
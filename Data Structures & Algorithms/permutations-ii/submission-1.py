from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs(curr)

                curr.pop()
                used[i] = False
        
        dfs([])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1,1,2]))
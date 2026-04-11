from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def dfs(i, subset):
            nonlocal total
            xor = 0
            for num in subset:
                xor ^= num
            
            total += xor

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1,subset)
                subset.pop()
        
        dfs(0, [])
        return total

        
if __name__ == "__main__":
    s = Solution()
    print(s.subsetXORSum([1, 3]))
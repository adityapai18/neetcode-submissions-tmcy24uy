from collections import deque, defaultdict, Counter
import heapq
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
            
        subsets = [0] * k

        def dfs(idx):
            if idx == len(nums):
                return True
            
            for i in range(k):
                if subsets[i] + nums[idx] <= target:
                    subsets[i] += nums[idx]

                    if dfs(idx + 1):
                        return True
                    
                    subsets[i] -= nums[idx]
                
                if subsets[i] == 0:
                    break

            return False
    
        return dfs(0)





if __name__ == "__main__":
    s = Solution()
    print(s.canPartitionKSubsets([2,4,1,3,5], 3))
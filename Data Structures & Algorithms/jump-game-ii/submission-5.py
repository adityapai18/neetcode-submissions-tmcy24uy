from collections import deque, defaultdict, Counter
import heapq
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)

        r,l = 0 , 0
        jumps = 0
        while r < n - 1:
            farthest =  0
            
            for i in range(l, r+ 1):
                farthest = max(farthest,i + nums[i])
            
            l = r+ 1
            r = farthest
            jumps+=1

        return jumps

if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))
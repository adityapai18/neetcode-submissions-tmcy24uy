from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degree = [0] * n
        out_degree = [0] * n

        for a , b in trust:
            out_degree[a - 1]+=1
            in_degree[b - 1]+=1
        
        for i , degree in enumerate(zip(out_degree, in_degree)):
            out , ind = degree
            if out == 0 and ind == n - 1:
                return i + 1
        
        return -1
        
if __name__ == "__main__":
    s = Solution()
    print(s.findJudge(2, [[1, 2]]))  # Output: 2
    print(s.findJudge(3, [[1, 3], [2, 3]]))  # Output: 3
    print(s.findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # Output:
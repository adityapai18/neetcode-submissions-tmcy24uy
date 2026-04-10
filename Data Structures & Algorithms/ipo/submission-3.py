from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w < min(capital):
            return w
        
        zipped_array = list(zip(capital,profits))

        zipped_array.sort(key = lambda x:x[0], reverse = True)

        max_profit_heap = []

        while max_profit_heap or zipped_array:
            if k == 0:
                break

            while zipped_array and zipped_array[-1][0] <= w:
                heapq.heappush(max_profit_heap,-zipped_array.pop()[1])

            if not max_profit_heap:
                break

            w = w - heapq.heappop(max_profit_heap)

            k-=1
        return w


if __name__ == "__main__":
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
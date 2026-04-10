from collections import deque, defaultdict, Counter
import heapq
from typing import List

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = []

        for char, cnt in count.items():
            heapq.heappush(maxHeap, [-cnt, char])

        res = ''
        prev = []
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)

            res+= char
            cnt+=1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt < 0:
                prev = [cnt, char]
        
        return res
            



        
if __name__ == "__main__":
    s = Solution()
    print(s.reorganizeString("aab"))
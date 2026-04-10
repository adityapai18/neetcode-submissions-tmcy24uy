from collections import deque, defaultdict
import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = []

        for i, t in enumerate(tasks):
            indexed_tasks.append([t[0],t[1],i])
        
        indexed_tasks.sort(key = lambda x:x[0], reverse=True)


        minHeap = []
        res =[]
        curr = 0

        while minHeap or indexed_tasks:
            if not minHeap and indexed_tasks and indexed_tasks[-1][0] > curr:
                curr = indexed_tasks[-1][0]
            
            while indexed_tasks and indexed_tasks[-1][0] <= curr:
                enq, proc, ind = indexed_tasks.pop()
                heapq.heappush(minHeap,[proc,ind])
            
            if minHeap:
                proc, ind = heapq.heappop(minHeap)
                res.append(ind)
                curr+= proc
        
        return res


               
        
if __name__ == "__main__":
    s = Solution()
    print(s.getOrder([[1,2],[2,3],[3,1]]))
from collections import deque, defaultdict, Counter
import heapq
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for trip in trips:
            pasng, start, end = trip
            events.append([start, pasng])
            events.append([end, -pasng])
        
        events.sort()

        curr = 0
        for event in events:
            curr+= event[1]
            if curr > capacity:
                return False
        
        return True
from collections import deque, defaultdict, Counter
import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, - num)
        heapq.heappush(self.right, - heapq.heappop(self.left))

        if len(self.right) > len(self.left):
            heapq.heappush(self.left, - heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return (- self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]
        
        

if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # return 2.0
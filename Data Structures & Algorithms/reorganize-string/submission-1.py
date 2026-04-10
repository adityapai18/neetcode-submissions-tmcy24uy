from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = []

        for char, cnt in count.items():
            heapq.heappush(maxHeap, [-cnt, char])

        res = [] # Using a list is more efficient than string concatenation
        prev = None
        
        # FIX: Continue as long as there is something in the heap OR something waiting
        while maxHeap or prev:
            # If we have a character waiting but nothing in the heap to separate it
            if not maxHeap and prev:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res.append(char)
            cnt += 1
            
            # Put the previously waiting character back into the pool
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            # If current character still has remaining counts, put it in waiting
            if cnt < 0:
                prev = [cnt, char]
        
        return "".join(res)

if __name__ == "__main__":
    s = Solution()
    print(s.reorganizeString("aab")) # Output: "aba"
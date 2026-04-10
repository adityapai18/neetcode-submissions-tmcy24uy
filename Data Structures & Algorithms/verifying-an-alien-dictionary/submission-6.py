from collections import deque, defaultdict, Counter
import heapq
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = { c: i for i ,c in enumerate(order) }

        for i in range(len(words) - 1):
            w1, w2 = words[i] , words[i+1]

            iter_len = min(len(w1), len(w2))

            if w1[:iter_len] == w2[:iter_len] and len(w1) > len(w2):
                return False

            for j in range(iter_len):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
        
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAlienSorted(["neetcode","neet"], "hlabcdefgijkmnopqrstuvwxyz"))
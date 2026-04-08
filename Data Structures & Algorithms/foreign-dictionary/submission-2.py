from collections import deque, defaultdict
import heapq
from typing import List
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = {c: set() for w in words for c in w}

        for i in range(n - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = ""

        def dfs(char):
            nonlocal res
            if char in visited:
                return visited[char] == False
            
            visited[char] = False

            for nei in graph[char]:
                if dfs(nei):
                    return True
            
            visited[char] = True

            res += char
        
        for char in graph:
            if dfs(char):
                return ""
        
        return res[::-1]

            


                        
if __name__ == "__main__":
    s = Solution()
    print(s.foreignDictionary(["wrt","wrf","er","ett","rftt"]))
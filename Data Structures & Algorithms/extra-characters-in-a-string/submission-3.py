from collections import deque, defaultdict, Counter
import heapq
from typing import List

class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        root = TreeNode()

        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TreeNode()
                node = node.children[char]
            node.is_word = True
        
        memo = {}
        def dfs(i):
            if i == len(s):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = 1 + dfs(i + 1)

            curr_node = root
            for j in range(i, len(s)):
                if s[j] not in curr_node.children:
                    break

                curr_node = curr_node.children[s[j]]

                if curr_node.is_word:
                    res = min(res, dfs(j+1))
            
            memo[i] = res
            
            return memo[i]

        return dfs(0)

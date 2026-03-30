class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        word_set = set(wordDict)
        def dfs(pointer, path):
            if pointer == len(s):
                res.append(" ".join(path))
                return
            
            for end in range(pointer + 1, len(s) + 1):
                current_word = s[pointer:end]

                if current_word in word_set:
                    path.append(current_word)
                    dfs(end,path)
                    path.pop()
        
        dfs(0,[])

        return res
                    
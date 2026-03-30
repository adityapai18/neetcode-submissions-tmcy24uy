class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(_open,close):
            if _open == close == n:
                res.append(''.join(stack))
                return
            
            if _open < n:
                stack.append('(')
                dfs(_open+1,close)
                stack.pop()
            if close < _open:
                stack.append(')')
                dfs(_open,close+1)
                stack.pop()
        
        dfs(0,0)
        return res

        
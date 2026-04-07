class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def generate(curr):
            res = []
            for i in range(4):
                digit = str((int(curr[i]) + 1) % 10) 
                res.append(curr[0:i] + digit + curr[i+1:])
                digit = str((int(curr[i]) - 1 )% 10)
                res.append(curr[0:i] + digit + curr[i+1:])
            
            return res

        q = deque([('0000',0)])
        visit = set(deadends)

        while q:
            curr , turns = q.popleft()
            if curr == target:
                return turns
            
            for val in generate(curr):
                if val not in visit:
                    visit.add(val)
                    q.append((val, turns + 1))
        
        return -1

                

        



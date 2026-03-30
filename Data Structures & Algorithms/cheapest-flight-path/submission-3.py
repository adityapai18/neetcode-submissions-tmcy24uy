class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        
        q = deque([(0,src,0)])

        while q:
            cst, node, hops = q.popleft()
            if hops > k:
                continue
            
            for nei, w in adj[node]:
                newCost = w + cst
                if newCost < prices[nei]:
                    prices[nei] = newCost
                    q.append((newCost, nei, hops + 1))
        
        return prices[dst] if prices[dst] != float("inf") else -1
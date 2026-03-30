class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0 # Initialize t to track the max time for a valid visit
        
        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)
            t = time # Update t only when we officially 'visit' a new node
            
            for val in edges[node]:
                if val[0] not in visit:
                    heapq.heappush(minHeap, (val[1] + time, val[0]))

        # Return t (the time of the last valid visit) if all nodes are reached
        return t if len(visit) == n else -1
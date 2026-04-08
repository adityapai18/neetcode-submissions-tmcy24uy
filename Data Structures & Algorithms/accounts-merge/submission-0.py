class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        inv_map = {}

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in inv_map:
                    inv_map[email] = name

        graph = defaultdict(list)
        for acc in accounts:
            for i in range(2, len(acc)):
                graph[acc[i]].append(acc[i-1])
                graph[acc[i-1]].append(acc[i])
        
        visited = set()
        res = []
        for email in inv_map:
            if email not in visited:
                visited.add(email)
                q = deque([email])
                emails = []
                while q:
                    node = q.popleft()
                    emails.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                res.append([inv_map[email]] + sorted(emails))
        return res



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        seen = set()
        q = deque([source])
        count = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for child in graph[node]:
                if child not in seen:
                    q.append(child)
                    seen.add(child)

        return False
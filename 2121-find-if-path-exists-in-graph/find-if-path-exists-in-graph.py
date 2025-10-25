class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0:
            return True
        paths = defaultdict(list)
        q = deque([source])
        seen = set()
        for i,j in edges:
            paths[i].append(j)
            paths[j].append(i)
        
        while q:
            node = q.popleft()
            if node in paths:
                if node == destination:
                    return True
                for child in paths[node]:
                    if child not in seen:
                        q.append(child)
                        seen.add(child)

        return False
        

        
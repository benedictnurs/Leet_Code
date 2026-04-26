class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        seen = set()
        def bfs(row, col):
            q = deque([(row, col)])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            start_letter = grid[row][col]
            print(start_letter)
            while q:
                r, c = q.popleft()
                visited[r][c] = True

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m:

                        if visited[nr][nc] == True:
                            continue
                        if grid[nr][nc] != start_letter:
                            continue
                        if (nr, nc) in seen:
                            return True
                        seen.add((nr, nc))
                        q.append((nr,nc))
            return False


        for row in range(n):
            for col in range(m):
                if not visited[row][col]:
                    if bfs(row, col) == True:
                        return True

        return False
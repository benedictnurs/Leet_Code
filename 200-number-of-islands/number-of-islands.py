class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        
        def bfs(row, col):
            q = deque([(row, col)])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] == "0":
                        continue
                    else:
                        q.append((nr,nc))
                        grid[nr][nc] = "0"
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1
        return count

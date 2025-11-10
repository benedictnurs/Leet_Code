class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sol = 0
        n, m = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque([(row,col)])
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            grid[row][col] = 0
            count = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        count += 1
                        q.append((nr,nc))
                        grid[nr][nc] = 0
            nonlocal sol
            if count > sol:
                sol = count
            return count
            
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    bfs(row,col)


        return sol

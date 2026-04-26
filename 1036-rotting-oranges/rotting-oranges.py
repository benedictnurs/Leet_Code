class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        time = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))


        while q:
            r,c,t = q.popleft()
            time = t
            for dr, dc in directions:
                nr,nc = dr+r,dc+c
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))

        for i in grid:
            if 1 in i:
                return -1

        return time

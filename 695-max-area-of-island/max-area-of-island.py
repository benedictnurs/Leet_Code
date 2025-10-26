class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sol = 0
        curr = 0
        n, m = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row+1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row,col-1)
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    sol = max(dfs(r,c), sol)
        return sol

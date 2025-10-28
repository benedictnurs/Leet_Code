class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or n <= r or c < 0 or m <= c or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row,col)
        return count
            
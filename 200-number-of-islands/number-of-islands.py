class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        count = 0
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)



        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        return count
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        sol = []
        max_vals = []

        for j in range(n - 2):
            for i in range(m - 2):
                subgrid = [row[i:i+3] for row in grid[j:j+3]]
                max_vals.append(max(sum(subgrid,[])))
        for i in range(0, len(max_vals), (m-2)):
            sol.append(max_vals[i:i+(m-2)])
        return sol
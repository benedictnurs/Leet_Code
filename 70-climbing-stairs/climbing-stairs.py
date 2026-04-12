class Solution:
    def climbStairs(self, n: int) -> int:
        sol = [1, 2]
        ans = []
        if n <= 2:
            return n

        for i in range(2, n):
            sol.append(sol[i-1] + sol[i-2])
        print(sol)
        return sol[-1]
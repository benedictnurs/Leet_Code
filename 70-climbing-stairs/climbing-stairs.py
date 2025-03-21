class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[-1]

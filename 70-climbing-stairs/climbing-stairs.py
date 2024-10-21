"""
DP

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n + 2)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
            
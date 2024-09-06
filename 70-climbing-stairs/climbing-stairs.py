class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        sol = [0] * (n+2)
        sol[0] = 0
        sol[1] = 1

        for i in range(2, n+2):
            sol[i] = sol[i-1] + sol[i-2]
        
        print(sol) 
        return sol[-1]
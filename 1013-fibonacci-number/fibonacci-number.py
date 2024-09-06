class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        sol = [0] * (n + 1)
        sol[0] = 0
        sol[1] = 1


        for i in range(2,n + 1):
            sol[i] = sol[i-1] + sol[i-2]
        
        print(sol)
        return sol[-1]
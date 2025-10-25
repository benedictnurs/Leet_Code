class Solution:
    def fib(self, n: int) -> int:
        if n == 2 or n == 1:
            return 1
        elif n == 0:
            return 0

        sol = [0 for _ in range(n+1)]
        sol[0] = 0
        sol[1] = 1

        for i in range(2, len(sol)):
            sol[i] = sol[i-1] + sol[i-2]

        return sol[-1]
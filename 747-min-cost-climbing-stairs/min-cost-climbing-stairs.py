class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)+1
        sol = [0] * n
        print(sol)
        sol[0] = 0
        sol[1] = 0

        for i in range(2, n):
            sol[i] = (min(sol[i-1]+cost[i-1],sol[i-2]+cost[i-2]))
        
        return sol[n-1]
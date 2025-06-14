class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Greedy problem
        # Set to inf
        # Find the minimum
        # If there is a negative version compare it to 
        # see if it is the same as the current sol
        sol = float(inf)

        for i in nums:
            if abs(sol) > abs(i):
                sol = i
            if abs(sol) == abs(i):
                sol = max(sol, i)
                
        return sol
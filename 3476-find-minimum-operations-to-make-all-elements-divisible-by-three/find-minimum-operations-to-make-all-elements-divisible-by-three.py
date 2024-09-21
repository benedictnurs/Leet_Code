class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sol = 0

        for i in nums:
            sol += (min(3-(i%3), i%3))
        return sol 
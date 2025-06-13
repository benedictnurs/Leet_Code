class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = float(-inf)
        curr = 0

        for i in nums:
            curr += i
            sol = max(sol, curr)
            if (curr) < 0:
                curr = 0

        return sol
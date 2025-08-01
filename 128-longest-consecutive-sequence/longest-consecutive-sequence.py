class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = 0
        numbers = set(nums)

        for i in numbers:
            curr = i
            curr_sol = 0
            if curr - 1 not in numbers:
                while curr in numbers:
                    curr += 1
                    curr_sol += 1
            sol = max(sol, curr_sol)
        return sol
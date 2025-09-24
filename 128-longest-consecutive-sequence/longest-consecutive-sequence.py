class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = 0
        numbers = set(nums)

        for num in numbers:
            curr = num
            count = 0
            
            if curr - 1 not in numbers:
                while curr in numbers:
                    curr += 1
                    count += 1
            sol = max(sol, count)

        return sol
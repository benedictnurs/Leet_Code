class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = 0
        numbers = set(nums)

        for number in numbers:
            if number - 1 not in numbers:
                curr = number
                count = 1

                while number + 1 in numbers:
                    number += 1
                    count += 1

                sol = max(sol, count)

        return sol
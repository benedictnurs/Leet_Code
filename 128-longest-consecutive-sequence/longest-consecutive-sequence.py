class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        sol = 0


        for i in nums:
            if i - 1 not in nums:
                curr = 1
                while (i+1) in nums:
                    curr += 1
                    i += 1
                sol = max(sol, curr)
        
        return (sol)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        sol = 0

        for r in range(len(nums)):
            while nums[r] in seen:
                if nums[l] in seen:
                    seen.remove(nums[l])
                l += 1
            sol = max(sol, sum(nums[l:r+1]))
            seen.add(nums[r])

        return sol
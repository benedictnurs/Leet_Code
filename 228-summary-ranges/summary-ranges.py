class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r = 0 ,0 
        sol = []
        while r < len(nums):
            if nums[r] + 1 not in nums:
                if nums[l] == nums[r]:
                    sol.append(str(nums[l]))
                else:
                    sol.append(f"{nums[l]}->{nums[r]}")
                l = r + 1
            r += 1
        print(sol)
        return sol

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        sol = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                sol.append(nums[l]**2)
                l += 1
            else:
                sol.append(nums[r]**2)
                r -= 1
        sol.reverse()
                
        return sol
        
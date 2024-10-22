class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = sum(nums)
        right = 0
        sol = []

        for i in nums:
            left -= i
            sol.append(abs(left - right))
            right += i

        return sol
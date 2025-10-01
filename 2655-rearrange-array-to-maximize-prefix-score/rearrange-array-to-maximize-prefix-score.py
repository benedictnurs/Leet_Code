class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix = nums[0]
        arr = [nums[0]]
        sol = 0

        for i in range(1, len(nums)):
            prefix += nums[i]
            arr.append(prefix)

        for i in arr:
            if i > 0:
                sol += 1

        return sol

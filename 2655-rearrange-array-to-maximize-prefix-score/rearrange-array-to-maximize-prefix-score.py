class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix = nums[0]
        # arr = [nums[0]]
        sol = 0
        if prefix > 0:
            sol += 1

        for i in range(1, len(nums)):
            prefix += nums[i]
            if prefix > 0:
                sol += 1
            # arr.append(prefix)


        return sol

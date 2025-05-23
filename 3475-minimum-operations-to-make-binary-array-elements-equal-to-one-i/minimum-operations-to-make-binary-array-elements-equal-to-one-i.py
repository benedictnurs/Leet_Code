class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sol = 0

        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                sol += 1
        if all(num == 1 for num in nums):
            return (sol)
        return -1
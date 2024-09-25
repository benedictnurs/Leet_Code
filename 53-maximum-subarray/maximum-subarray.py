class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = 0
        current = 0

        if all(x < 0 for x in nums):
            return max(nums)

        if len(nums) == 1:
            return nums[0]
        for i in nums:
            current += i
            largest = max(current, largest)
            if current < 0:
                current = 0
        
        return largest
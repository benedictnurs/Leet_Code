class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float("-inf")
        current = 0

        if len(nums) == 1:
            return nums[0]
        for i in nums:
            current += i
            largest = max(current, largest)
            if current < 0:
                current = 0
        
        return largest
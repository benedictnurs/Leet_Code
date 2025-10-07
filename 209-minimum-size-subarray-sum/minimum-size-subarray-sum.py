class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = float('inf')
        count = 0

        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                count -= nums[l]
                curr = min(curr, r-l+1)
                l += 1
        if curr != float('inf'): 
            return curr
        else:
            return 0

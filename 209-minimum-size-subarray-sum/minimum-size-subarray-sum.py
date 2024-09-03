class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = float("inf")
        count = 0
        
        for r in range(len(nums)):
            count += nums[r]
            if count >= target:
                ans = min(r-l+1,ans)

            while count >= target and l < len(nums):
                count -= nums[l]
                ans = min(r-l+1,ans)
                l += 1


        if ans == float("inf"):
            return 0
        
        return ans
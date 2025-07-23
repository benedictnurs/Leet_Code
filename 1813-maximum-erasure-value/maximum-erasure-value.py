class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        curr = 0 
        best = 0
        
        for r in range(len(nums)):
            x = nums[r]
            while x in seen:
                seen.remove(nums[l])
                curr -= nums[l]
                l += 1
            
            seen.add(x)
            curr += x
            best = max(best, curr)
        
        return best
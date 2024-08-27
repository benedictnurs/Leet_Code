class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        indx = 0
        window = sum(nums[indx:k])
        ans = window/k

        for i in range(k, len(nums)):
            window = window + nums[i] - nums[indx]
            ans = max(ans,window/k)           
            indx += 1
        
        return ans
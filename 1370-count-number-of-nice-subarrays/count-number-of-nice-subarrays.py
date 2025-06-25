class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = 0
        l = 0
        odd = 0
        m = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odd += 1

            while odd > k:
                if nums[l] % 2 != 0:
                    odd -= 1
                l += 1
                m = l
            
            if k == odd:
                while nums[m] %2 == 0:
                    m += 1
            
                count += (m-l+1)
                
        return count
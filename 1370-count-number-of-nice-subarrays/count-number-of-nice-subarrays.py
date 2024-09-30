class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        m = 0
        sol = 0
        odd = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odd += 1
            
            while odd > k:
                if nums[l] % 2 != 0:
                    odd -= 1
                l += 1
                m = l

            if odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                sol += ((m - l) + 1)

        return sol
 

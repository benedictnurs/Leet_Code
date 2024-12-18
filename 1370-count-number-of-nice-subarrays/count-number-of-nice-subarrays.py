class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        odd = 0
        sol = 0
        for i in nums:
            if i % 2 != 0:
                odd += 1

            if odd-k in hm:
                sol += hm[odd-k]
            
            if odd in hm:
                hm[odd] += 1
            else:
                hm[odd] = 1
        return sol

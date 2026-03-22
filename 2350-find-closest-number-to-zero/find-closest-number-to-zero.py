class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            if abs(i) in hm:
                hm[abs(i)].append(i)
            else:
                hm[abs(i)] = [i]

        
        return (max(hm[min(hm.keys())]))
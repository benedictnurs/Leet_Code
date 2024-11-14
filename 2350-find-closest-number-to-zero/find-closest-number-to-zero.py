class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            if abs(i) not in hm:
                hm[abs(i)] = [i]
            else:
                hm[abs(i)].append(i)
        return max(hm[(min(hm))])

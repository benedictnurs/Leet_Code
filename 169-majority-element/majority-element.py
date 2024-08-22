class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for i in set(nums):
            hm[nums.count(i)] = i
        return(hm[max(hm.keys())])         

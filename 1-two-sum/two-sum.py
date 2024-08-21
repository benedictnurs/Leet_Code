class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,j in enumerate(nums):
            if target - j in hm:
                return [i, hm[target-j]]
            hm[j] = i
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            end = target - nums[i]
            if end in hm:
                return(hm[end], i)
            hm[nums[i]] = i
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]

        for i in range(len(nums)-1):
            res.append(res[i] + nums[i+1])

        return (res)

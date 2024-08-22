class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = [float(-inf),0]
        for i in set(nums):
            ans = max(ans,[nums.count(i),i])
        return(ans[1])

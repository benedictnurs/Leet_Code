class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        ans = [float(-inf),0]
        for i in set(nums):
            hm[nums.count(i)] = i
            ans = max(ans,[nums.count(i),i])
        return(ans[1])

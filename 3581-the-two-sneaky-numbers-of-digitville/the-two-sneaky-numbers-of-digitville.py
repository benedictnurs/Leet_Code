class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2+1):
            temp = (nums[i:i+2])
            if temp[0] == temp[1]:
                ans.append(nums[i])
        return ans
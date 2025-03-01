class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0
        sol = []
        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                nums[l] = nums[l] * 2
                nums[r] = 0
            l += 1
        print(nums)
        for i in nums:
            if i != 0:
                sol.append(i)
        for i in range(nums.count(0)):
            sol.append(0)
        
        return sol
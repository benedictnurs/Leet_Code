class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            sol[i] *= prefix
            prefix *= nums[i]
        print(sol)

        postfix = 1
        n = len(nums) - 1
        while n:
            print(postfix)
            sol[n] *= postfix
            postfix *= nums[n]
            n -= 1
        sol[0] *= postfix
        
        return sol
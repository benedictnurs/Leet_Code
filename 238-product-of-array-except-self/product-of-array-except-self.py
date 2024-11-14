class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = [1] * n

        prefix = 1
        for i in range(n):
            sol[i] = prefix
            prefix *= nums[i]
        r = n - 1
        print(sol)

        postfix = 1
        while r > 0:
            postfix *= nums[r] 
            r -= 1
            sol[r] *= postfix

        return (sol)
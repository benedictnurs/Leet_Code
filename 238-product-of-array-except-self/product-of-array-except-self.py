class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numbers = []

        curr = 1
        for i in nums:
            numbers.append(curr)
            curr*=i

        n = len(nums) - 1
        prev = 1
        while n:
            prev *= nums[n]
            n-=1
            numbers[n] *= prev
            # print(prev, numbers[n])
        return (numbers)
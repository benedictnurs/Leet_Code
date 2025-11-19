class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        curr = original*2
        if original not in nums:
            return original

        for i in range(len(nums)):
            print(curr)
            if (curr) not in nums:
                return curr
            curr *= 2

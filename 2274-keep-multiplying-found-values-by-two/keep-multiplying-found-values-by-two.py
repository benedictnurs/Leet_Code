class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        curr = original*2
        if original not in nums:
            return original

        for i in range(len(nums)):
            if (curr) not in nums:
                return curr
            curr *= 2

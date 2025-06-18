class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        res = []

        def backtrack(i):
            if len(res) == len(nums):
                sol.append(res[:])
                return

            for i in range(len(nums)):
                if nums[i] not in res:
                    res.append(nums[i])
                    backtrack(i+1)
                    res.pop()

        backtrack(0)
        return sol
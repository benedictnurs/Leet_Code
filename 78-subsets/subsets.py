class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        res = []


        def backtrack(start):
            sol.append(res[:])
            
            for i in range(start, len(nums)):
                res.append(nums[i])
                backtrack(i + 1)
                res.pop()


        backtrack(0)
        return sol
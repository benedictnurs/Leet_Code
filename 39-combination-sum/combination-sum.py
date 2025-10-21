class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []

        def backtrack(index, value):
            if value == target:
                sol.append(res[:])
            
            if value > target:
                return
            
            for i in range(index, len(candidates)):
                res.append(candidates[i])
                backtrack(i, candidates[i]+value)
                res.pop()

        backtrack(0,0)
        return sol     



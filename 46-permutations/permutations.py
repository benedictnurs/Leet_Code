class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, curr = [], []
        def backtrack():
            if n == len(curr):
                sol.append(curr[:])
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack()
                    curr.pop()
        backtrack()
        return sol
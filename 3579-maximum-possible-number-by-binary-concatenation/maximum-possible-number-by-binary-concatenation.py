class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        lst = ["{0:b}".format(i) for i in nums]
        sol = float(-inf)
        for combo in permutations(lst):
            concatenated = ''.join(combo)
            sol = max(sol, int(concatenated, 2))

        return sol
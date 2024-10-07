class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        lst = ["{0:b}".format(i) for i in nums]
        sol = float(-inf)
        for combo in itertools.permutations(lst, 3):
            concatenated = ''.join(combo)
            print(int(concatenated, 2))
            sol = max(sol, int(concatenated, 2))
            
        return sol
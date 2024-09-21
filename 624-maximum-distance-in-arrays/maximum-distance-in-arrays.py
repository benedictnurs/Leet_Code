class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = arrays[0][0]
        big = arrays[0][-1]
        sol = 0

        for i in range(1, len(arrays)):
            sol = max(sol , abs(arrays[i][-1] - small), abs(big - arrays[i][0]))
            small = min(small, arrays[i][0])
            big = max(big, arrays[i][-1])
        
        return sol
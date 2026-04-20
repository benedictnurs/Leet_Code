class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        sol = 0

        for i in range(len(colors)):
            for j in range(1, len(colors)):
                if colors[i] != colors[j]:
                    sol = max(sol, abs(i-j))


        return sol
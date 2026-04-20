class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist1, dist2 = 0, 0
        n = len(colors)

        for i in range(n):
            if colors[i] != colors[-1]:
               dist1 = max(dist1, (abs(i - n + 1)))
        
        for j in range(n-1, -1, -1):
            if colors[j] != colors[0]:
                dist2 = max(dist2, j)

        return max(dist1, dist2)
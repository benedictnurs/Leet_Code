class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2
        counts = {}
        for i in range(1, n + 1):
            counts[i] = 0

        for i in grid:
            for j in i:
                counts[j] += 1

        sol = []
        sorted_counts  = sorted(counts.items(),  key = lambda x: x[1], reverse=True)
        for i in sorted_counts:
            if i[1] >= 2:
                sol.append(i[0])
            if i[1] == 0:
                sol.append(i[0])

        return (sol)
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        maxs = []
        mins = set()
        for c in range(len(matrix[0])):
            maximum = float("-inf")
            for r in range(len(matrix)):
                maximum = max(maximum, matrix[r][c])
                mins.add(min(matrix[r]))
            maxs.append(maximum)
        return list(mins & set(maxs))
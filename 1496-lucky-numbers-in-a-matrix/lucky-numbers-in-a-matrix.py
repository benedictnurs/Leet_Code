class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = {min(row) for row in matrix}
        
        col_maxs = set()
        for c in range(len(matrix[0])):
            maximum = float("-inf")
            for r in range(len(matrix)):
                maximum = max(maximum, matrix[r][c])
            col_maxs.add(maximum)
        
        return list(row_mins & col_maxs)

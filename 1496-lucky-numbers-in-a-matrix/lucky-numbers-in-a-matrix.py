class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum in each row
        row_mins = {min(row) for row in matrix}
        
        # Step 2: Find the maximum in each column
        col_maxs = set()
        for c in range(len(matrix[0])):
            maximum = float("-inf")
            for r in range(len(matrix)):
                maximum = max(maximum, matrix[r][c])
            col_maxs.add(maximum)
        
        # Step 3: Return the intersection of row mins and column maxs
        return list(row_mins & col_maxs)

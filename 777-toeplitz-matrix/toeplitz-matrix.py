class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # 00 11 22, 01 12 23, 02 13
        n = len(matrix)
        col = len(matrix[0])
        row = len(matrix)

        for c in range(1, col):
            for r in range(1, row):
                if (matrix[r][c]) != matrix[r-1][c-1]:
                    return False
        
        return True
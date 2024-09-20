class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        sol = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                sol[col][row] = matrix[row][col]

        return sol

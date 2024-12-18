class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        sol = [[0] * n for _ in range(m)] 
        print(sol)

        for row in range(n):
            for col in range(m):
                sol[col][row] = matrix[row][col]
        return sol

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        sol = []

        for col in range(m):
            temp = []
            for row in range(n):
                temp.append(matrix[row][col])
            sol.append(temp)
        return sol

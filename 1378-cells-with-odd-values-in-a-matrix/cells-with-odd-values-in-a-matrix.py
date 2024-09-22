class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0]*n for _ in range(m) ]
        sol = 0
        for i in range(len(indices)):
            row = indices[i][0]
            col = indices[i][1]

            for r in range(len(matrix[0])):
                matrix[row][r] += 1        

            for c in range(len(matrix)):
                matrix[c][col] += 1        
        print(matrix)

        for i in sum(matrix,[]):
            if i % 2 != 0:
                sol += 1

        return sol
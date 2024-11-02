class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [[1]]

        for i in range(numRows-1):
            temp = [0] + sol[-1] + [0]
            row = []

            for j in range(1, len(temp)):
                row.append(temp[j]+temp[j-1])
            print(row)
            sol.append(row)
        
        return sol
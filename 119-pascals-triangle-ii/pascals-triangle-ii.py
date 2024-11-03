class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        sol = [[1]]

        for i in range(rowIndex):
            temp = [0] + sol[-1] + [0]
            curr = []
            for i in range(1, len(temp)):
                curr.append(temp[i-1]+temp[i])
            sol.append(curr)
        return sol[-1]
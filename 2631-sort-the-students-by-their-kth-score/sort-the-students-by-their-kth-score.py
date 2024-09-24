class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        hm = {}
        sol = []
        for row in range(len(score)):
            column = []
            for col in range(len(score[0])):
                column.append(score[row][col])
            hm[row] = (column[k], column)

        for ranking, row in sorted(hm.values(), key=lambda x: x[0], reverse = True):
            print(ranking, row)
            sol.append(row)
        
        return sol
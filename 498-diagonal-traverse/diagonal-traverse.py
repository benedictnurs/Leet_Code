class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hm = {}
        sol = []
        
        for c in range(len(mat)):
            for r in range(len(mat[0])):
                v = c + r
                if v not in hm:
                    hm[v] = [mat[c][r]]
                else:
                    hm[v].append(mat[c][r])
                
        direct = 1
        for k, v in hm.items():
            if direct == -1:
                sol.extend(v)
                direct = 1
            elif direct == 1:
                sol.extend(v[::-1])
                direct = -1   

        return (sol)
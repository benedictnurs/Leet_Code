class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hm = {}
        sol = []
        for i in range(len(mat)):
            hm[i] = (sum(mat[i]))
        silly = (sorted(hm.items(), key=lambda x: x[1]))
        for i in range(k):
            sol.append(silly[i][0])
        return(sol)
            

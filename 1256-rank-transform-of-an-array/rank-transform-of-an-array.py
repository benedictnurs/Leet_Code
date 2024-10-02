class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hm = {}
        sol = []

        ranked = sorted(set(arr))

        for v,i in enumerate(ranked):
            hm[i] = (v+1)

        for i in arr:
            sol.append(hm[i])

        return sol
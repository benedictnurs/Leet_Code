class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm = {}
        sol = float(inf)
        for i in set(text):
            if i in "balloon":
                hm[i] = text.count(i)
        if (len(hm)) != 5:
            return 0

        for k, v in hm.items():
            if k == "o" or k == "l":
                sol = min(sol, (v//2))
            else:
                sol = min(sol, v)
        return sol
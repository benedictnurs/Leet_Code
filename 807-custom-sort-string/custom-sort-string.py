class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {}
        sett = set(list(s))
        lst = list(s)
        sol = ""
        for i in range(len(order)):
            hm[i] = order[i]

        print(hm)

        for k, v in hm.items():
            if v in sett:
                sol += (v)*s.count(v)
                sett.remove(v)

        new = sorted(sett)
        newlst = (sorted(lst))

        for i in new:
            sol += i*newlst.count(i)

        return sol
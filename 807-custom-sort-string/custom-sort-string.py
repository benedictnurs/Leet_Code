class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderLst = []
        sett = set(list(s))
        lst = list(s)
        sol = ""
        
        for i in range(len(order)):
            orderLst.append(order[i])

        for i in orderLst:
            if i in sett:
                sol += (i)*s.count(i)
                sett.remove(i)

        new = sorted(sett)
        lst.sort()
        
        for i in sorted(sett):
            sol += i*lst.count(i)

        return sol
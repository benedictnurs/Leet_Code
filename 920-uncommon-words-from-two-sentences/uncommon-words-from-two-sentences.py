class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        sol = []
        hm = {}

        for i in s1:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        for i in s2:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        for k, v in hm.items():
            if v == 1:
                sol.append(k)
    
        print(sol)
        return sol
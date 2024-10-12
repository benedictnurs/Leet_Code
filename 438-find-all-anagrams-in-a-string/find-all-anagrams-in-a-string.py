class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        find = sorted(p)
        k = len(p)
        sol = []
        for i in range(len(s)-k+1):
            inhere = sorted(s[i:i+k])
            if find == inhere:
                sol.append(i)
        return sol
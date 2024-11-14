class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm = {}
        sol = []

        for i in range(len(s)-9):
            dna = (s[i:i+10])
            if dna not in hm:
                hm[dna] = 1
            else:
                hm[dna] += 1
                if dna not in sol:
                    sol.append(dna)
        return sol


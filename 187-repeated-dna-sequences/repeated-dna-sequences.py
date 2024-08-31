class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm = {}
        curr = []
        k = 10
        ans = []
        if k > len(s):
            return []
        
        for i in range(len(s)-k+1):
            dna = s[i:i+k]
            if dna not in hm:
                hm[dna] = 1
            else:
                hm[dna] += 1
        
        for k,v in hm.items():
            if v >= 2:
                ans.append(k)


        return (ans)

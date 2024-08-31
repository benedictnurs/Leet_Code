class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm = {}
        curr = []
        k = 10
        ans = []
        if k > len(s):
            return []
            
        for i in range(k):
            curr.append(s[i])
            dna = "".join(curr)
        hm[dna] = 1
        
        for i in range(k, len(s)):
            curr.pop(0)
            curr.append(s[i])
            dna = "".join(curr)
            if dna not in hm:
                hm[dna] = 1
            else:
                hm[dna] += 1
        
        for k,v in hm.items():
            if v >= 2:
                ans.append(k)


        return (ans)

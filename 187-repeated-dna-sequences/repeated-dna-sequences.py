class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        curr = []
        k = 10
        ans = []
        if k > len(s):
            return []
        
        for i in range(len(s)-k+1):
            dna = s[i:i+k]
            if dna in seen:
                seen.add(dna)
                if dna not in ans:
                    ans.append(dna)
            seen.add(dna)
        
    


        return (ans)

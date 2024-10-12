class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []

        for q in queries:
            l = 0
            good = True
            for r in range(len(q)):
                if l<len(pattern) and q[r] == pattern[l]:
                    l+=1
                elif q[r].isupper():
                    good = False
                    break
            ans.append(good and l==len(pattern))
        
        return ans
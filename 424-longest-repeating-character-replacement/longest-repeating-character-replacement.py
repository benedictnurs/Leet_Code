class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        l = 0
        sol = 0

        for r in range(len(s)):
            hm[s[r]] += 1
            maxFreq = max(hm.values())
            currLen = r-l+1
            if currLen - maxFreq > k:
                hm[s[l]] -= 1
                l += 1
            sol = max(sol, r-l+1)
        
        return sol
                            

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hm = {k:0 for k in "abc"}
        n = len(s)
        count = 0
        l = 0

        for r in range(n):
            hm[s[r]] += 1
       
            while all(i >= 1 for i in hm.values()):
                hm[s[l]] -= 1
                l += 1
            count += l

        return count
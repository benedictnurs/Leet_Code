class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hm = Counter()
        n = len(s)
        count = 0
        l = 0

        for r in range(n):       
            hm[s[r]] += 1
            while len(hm) == 3:
                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1
            count += l

        return count
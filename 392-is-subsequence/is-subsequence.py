class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        if s == "":
            return True
        for r in range(len(t)):
            if s[l] == t[r]:
                l += 1

                if len(s) == l:
                    return True
        return l == len(s)
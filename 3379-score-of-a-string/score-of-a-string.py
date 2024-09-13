class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        l = 0
        for r in range(1, len(s)):
            ans+=(abs(ord(s[l])-ord(s[r])))
            l+=1
        return (ans)

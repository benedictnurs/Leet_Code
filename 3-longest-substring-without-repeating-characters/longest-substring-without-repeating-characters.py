class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxx = 0

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                if s[l] in seen:
                    seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxx = max(maxx, r-l + 1)
        
        return maxx
                
        
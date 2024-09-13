class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        ans = 0
        
        for i in set(s):
            count = s.count(i)
            if count % 2 != 0:
                if "odd" not in hm:
                    hm["odd"] = count - 1
                else:
                    hm["odd"] += count - 1
            else:
                if "even" not in hm:
                    hm["even"] = count
                else:
                    hm["even"] += count
        
        return sum(hm.values()) + (1 if "odd" in hm else 0)


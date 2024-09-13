class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        ans = 0
        
        for i in set(s):
            count = s.count(i)
            if count % 2 != 0:
                # If odd count, subtract 1 to make it even
                if "odd" not in hm:
                    hm["odd"] = count - 1
                else:
                    hm["odd"] += count - 1
            else:
                if "even" not in hm:
                    hm["even"] = count
                else:
                    hm["even"] += count
        
        # If there's any odd character, we can add 1 more character to the center
        return sum(hm.values()) + (1 if "odd" in hm else 0)


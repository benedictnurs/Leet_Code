class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hm = Counter(words)
        count = 0
        center = False
        
        for k, v in hm.items():
            rev = k[::-1]
            if rev != k:
                count += 2*(min(hm[rev], v))
            else:
                pairs = v//2
                count += 4*pairs
                if v % 2 == 1:
                    center = True 

        if center == True:
            count += 2

        return count